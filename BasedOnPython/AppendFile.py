import os

copyright_haha = '''\
// --------------------------------------------------------------------------------------------------------------------
// <copyright file="$safeitemrootname$" company="HAHA">
// Copyright (c) HAHA 2006 - $year$
// </copyright>
// --------------------------------------------------------------------------------------------------------------------
// File Name        : $rootnamespace$.$safeitemrootname$
// Description      : 
//
// Revision History :
//     V0           : 
//         Author   : [$machinename$]$username$
//         Time     : $time$
//         Reason   : Create File
// --------------------------------------------------------------------------------------------------------------------

'''


def find_cs_files(file_dir):
    '''
    查找指定文件夹下的所有以.cs为扩展名的文件
    file_dir : 需要查找的文件夹
    '''
    cs_files = []
    for root, dirs, files in os.walk(file_dir):
        for cs_file in files:
            file_name, file_extension = os.path.splitext(cs_file)
            if file_extension == '.cs' and file_name != 'AssemblyInfo':
                full_name = os.path.join(root, cs_file)
                cs_files.append(full_name)
    return cs_files


def remove_old_comment(comment_lines):
    '''
    移除文件中原有的开始注释行与空行
    '''
    new_comment_lines = []
    for comment_line in comment_lines:
        comment_line = comment_line.encode('utf-8').decode('utf-8-sig')
        comment_line = str(comment_line)
        if '//' in comment_line:
            # 移除注释行
            continue
        elif len(comment_line) == 1 and comment_line.find('\n') != -1:
            # 移除空行
            continue
        else:
            new_comment_lines.append(comment_line)
    return new_comment_lines


def change_namespace_position(namespace_lines):
    '''将命名空间行提到文件的顶层'''
    namespace_length = len(namespace_lines)
    if namespace_length <= 1:
        # 仅有一行，不执行任何操作
        return namespace_lines

    if 'namespace' in namespace_lines[0]:
        # 说明namespace声明已在最外层，不执行任何操作
        return namespace_lines

    # 获取namespace关键字与其紧接着的左大括号在lines中的行索引
    index_namespace = -1
    index_first_bracket = -1
    for index in range(len(namespace_lines)):
        if 'namespace' in namespace_lines[index]:
            index_namespace = index
            if '{' in namespace_lines[index]:
                index_first_bracket = index
            else:
                index_first_bracket = index + 1
            break

    # 两个索引都存在的条件下，执行将namespace关键字和与之对应的左大括号提到最外层
    if index_namespace != -1 and index_first_bracket != -1:
        namespace = namespace_lines[index_namespace: index_first_bracket + 1]
        length = len(namespace)
        if length == 1:
            namespace_lines.remove(namespace[0])
            namespace_lines.insert(0, namespace[0])
        else:
            namespace_lines.remove(namespace[0])
            namespace_lines.remove(namespace[1])
            namespace_lines.insert(0, namespace[1])
            namespace_lines.insert(0, namespace[0])

    return namespace_lines

def add_tab_space_before_using(using_lines):
    '''
    在原始using语句前增加Tab，以保持格式相同
    '''

    # 查看namespace关键字与class, struct, enum, interface等关键字对应的左括号的索引
    index_first_bracket = -1
    index_second_bracket = -1
    for index in range(len(using_lines)):
        if index_first_bracket == -1 and '{' in using_lines[index]:
            index_first_bracket = index
        else:
            if index_first_bracket != -1 and '{' in using_lines[index]:
                index_second_bracket = index
                break

    modified = False
    for index in range(index_first_bracket, index_second_bracket):
        using_line = using_lines[index]
        if 'using' in using_line or '$endif$' in using_line:
            if not str(using_line).startswith('\t'):
                using_line = '\t' + using_line
                modified = True
                new_lines[index] = using_line
        elif modified:
            using_lines[index] = using_line
            using_lines.insert(index, '\n')
            break

    return using_lines



if __name__ == "__main__":
    files = find_cs_files(r'D:\\CSharp')
    for file in files:
        print(file)
        with open(file, mode='r+', encoding='utf-8') as f:
            lines = f.readlines()
            # 移除原有的开始注释行
            new_lines = remove_old_comment(lines)
            # 将命名空间行提到最外层
            new_lines = change_namespace_position(new_lines)
            # 增加using语句的缩进
            new_lines = add_tab_space_before_using(new_lines)

            # 插入版权信息
            new_lines.insert(0, copyright_haha)
            
            # for line in new_lines:
            #     print(line, end='')
            # print('-'*50)

            # 清空原文件
            f.seek(0, 0)
            f.truncate()
            
            # 写入新内容
            for line in new_lines:
                f.writelines(str(line))