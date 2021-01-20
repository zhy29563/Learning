'''
While OpenCV was designed for use in full-scale applications and can be used within functionally rich UI frameworks (such as Qt*, WinForms*, or Cocoa*) or without any UI at all, sometimes there it is required to try functionality quickly and visualize the results. This is what the HighGUI module has been designed for.

It provides easy interface to:
    ☯ Create and manipulate windows that can display images and "remember" their content (no need to handle repaint events from OS).
    ☯ Add trackbars to the windows, handle simple mouse events as well as keyboard commands.
'''

# ButtonCallback
# Callback function for a button created by cv::createButton.
# typedef void(* cv::ButtonCallback) (int state, void *userdata)
'''
Parameters
    state       current state of the button. It could be -1 for a push button, 0 or 1 for a check/radio box button.
    userdata    The optional parameter.
'''

# MouseCallback
# Callback function for mouse events. see cv::setMouseCallback.
# typedef void(* cv::MouseCallback) (int event, int x, int y, int flags, void *userdata)
'''
Parameters
    event       one of the cv::MouseEventTypes constants.
    x           The x-coordinate of the mouse event.
    y           The y-coordinate of the mouse event.
    flags       one of the cv::MouseEventFlags constants.
    userdata    The optional parameter.
'''

# OpenGlDrawCallback
# Callback function defined to be called every frame. See cv::setOpenGlDrawCallback.
# typedef void(* cv::OpenGlDrawCallback) (void *userdata)
'''
Parameters
    userdata    The optional parameter.
'''

# TrackbarCallback
# Callback function for Trackbar see cv::createTrackbar.
# typedef void(* cv::TrackbarCallback) (int pos, void *userdata)
'''
Parameters
    pos         current position of the specified trackbar.
    userdata    The optional parameter.
'''
import numpy as np
import cv2 as cv
###########################################################################################
# 创建命名窗口
###########################################################################################
# Creates a window.
# None  =   cv.namedWindow(winname[, flags])
# The function namedWindow creates a window that can be used as a placeholder for images and trackbars. 
# Created windows are referred to by their names.
# 
# If a window with the same name already exists, the function does nothing.
# 
# You can call cv::destroyWindow or cv::destroyAllWindows to close the window and de-allocate any associated memory usage.
# For a simple program, you do not really have to call these functions because all the resources and windows of the application are closed automatically by the operating system upon exit.
'''
Parameters
    winname Name of the window in the window caption that may be used as a window identifier.
    flags   Flags of the window. The supported flags are: (cv::WindowFlags)
'''
# WindowFlags
'''
cv.WINDOW_NORMAL
    the user can resize the window (no constraint) / also use to switch a fullscreen window to a normal size.

cv.WINDOW_AUTOSIZE
    the user cannot resize the window, the size is constrainted by the image displayed.

cv.WINDOW_OPENGL
    window with opengl support.

cv.WINDOW_FULLSCREEN
    change the window to fullscreen.

cv.WINDOW_FREERATIO
    the image expends as much as it can (no ratio constraint).

cv.WINDOW_KEEPRATIO
    the ratio of the image is respected.

cv.WINDOW_GUI_EXPANDED
    status bar and tool bar

cv.WINDOW_GUI_NORMAL
    old fashious way
'''
winname = 'test'
cv.namedWindow(winname, cv.WINDOW_GUI_EXPANDED | cv.WINDOW_NORMAL | cv.WINDOW_KEEPRATIO)

###########################################################################################
# 读取图像
###########################################################################################
mat = cv.imread('lena.png')


###########################################################################################
# 设置窗口标题
###########################################################################################
# Updates window title.
# None = cv.setWindowTitle(winname, title)
'''
Parameters
    winname Name of the window.
    title   New title.
'''
cv.setWindowTitle(winname, 'First OpenCV Window')

###########################################################################################
# 创建滑动条
###########################################################################################
# Creates a trackbar and attaches it to the specified window.
# The function createTrackbar creates a trackbar (a slider or range control) with the specified name and range,
# assigns a variable value to be a position synchronized with the trackbar and specifies the callback function
# onChange to be called on the trackbar position change. The created trackbar is displayed in the specified
# window winname.
'''
int cv::createTrackbar(const String &   trackbarname,
                       const String &   winname,
                       int *            value,
                       int              count,
                       TrackbarCallback onChange = 0,
                       void *           userdata = 0)

Parameters
    trackbarname    Name of the created trackbar.
    winname         Name of the window that will be used as a parent of the created trackbar.
    value           Optional pointer to an integer variable whose value reflects the position of the slider.
                    Upon creation, the slider position is defined by this variable.
    count           Maximal position of the slider. The minimal position is always 0.
    onChange        Pointer to the function to be called every time the slider changes position.
                    This function should be prototyped as void Foo(int,void*); , where the first parameter
                    is the trackbar position and the second parameter is the user data (see the next parameter).
                    If the callback is the NULL pointer, no callbacks are called, but only value is updated.
    userdata        User data that is passed as is to the callback. It can be used to handle trackbar events
                    without using global variables.
'''
def trackCallBack(state):
    print(state)
cv.createTrackbar('test', winname, 0, 255, trackCallBack)

###########################################################################################
# 设置鼠标回调
###########################################################################################
'''
void cv::setMouseCallback(const String & winname,
                          MouseCallback  onMouse,
                          void *         userdata = 0 )
Parameters
    winname     Name of the window.
    onMouse     Callback function for mouse events. See OpenCV samples on how to specify and use the callback.
    userdata    The optional parameter passed to the callback.
'''
def on_mouse(event ,x,y,flag,param):
    #print('(x,y)={},{}'.format(x, y))

    if event == cv.EVENT_MOUSEMOVE:
        #print('EVENT_MOUSEMOVE')
        pass
    elif event == cv.EVENT_LBUTTONDOWN:
        print('EVENT_LBUTTONDOWN')
        cv.setTrackbarMin('test', winname, 100)
    elif event == cv.EVENT_RBUTTONDOWN:
        print('EVENT_RBUTTONDOWN')
        cv.setTrackbarMax('test', winname, 255)
    elif event == cv.EVENT_MBUTTONDOWN:
        print('EVENT_MBUTTONDOWN')
        import random
        pos = random.randint(100, 255)
        cv.setTrackbarPos('test',winname, pos)
    elif event == cv.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP')
    elif event == cv.EVENT_RBUTTONUP:
        print('EVENT_RBUTTONUP')
    elif event == cv.EVENT_MBUTTONUP:
        print('EVENT_MBUTTONUP')
    elif event == cv.EVENT_LBUTTONDBLCLK:
        print('EVENT_LBUTTONDBLCLK')
    elif event == cv.EVENT_RBUTTONDBLCLK:
        print('EVENT_RBUTTONDBLCLK')
    elif event == cv.EVENT_MBUTTONDBLCLK:
        print('EVENT_MBUTTONDBLCLK')
    elif event == cv.EVENT_MOUSEWHEEL:
        print('EVENT_MOUSEWHEEL')

    if flag == cv.EVENT_FLAG_LBUTTON:
        print('EVENT_FLAG_LBUTTON')
    elif flag == cv.EVENT_FLAG_RBUTTON:
        print('EVENT_FLAG_RBUTTON')
    elif flag == cv.EVENT_FLAG_MBUTTON:
        print('EVENT_FLAG_MBUTTON')
    elif flag == cv.EVENT_FLAG_CTRLKEY:
        print('EVENT_FLAG_CTRLKEY')
    elif flag == cv.EVENT_FLAG_SHIFTKEY:
        print('EVENT_FLAG_SHIFTKEY')
    elif flag == cv.EVENT_FLAG_ALTKEY:
        print('EVENT_FLAG_ALTKEY')

cv.setMouseCallback(winname, on_mouse, None)


###########################################################################################
# 显示图像
###########################################################################################
# Displays an image in the specified window.
# None  =   cv.imshow(winname, mat)
'''
Parameters
    winname Name of the window.
    mat     Image to be shown.
'''
'''
The function imshow displays an image in the specified window. 
If the window was created with the cv::WINDOW_AUTOSIZE flag, the image is shown with its original size, 
however it is still limited by the screen resolution. Otherwise, the image is scaled to fit the window. 
The function may scale the image, depending on its depth:
    ☯ If the image is 8-bit unsigned, it is displayed as is.
    ☯ If the image is 16-bit unsigned or 32-bit integer, the pixels are divided by 256. 
       That is, the value range [0,255*256] is mapped to [0,255].
    ☯ If the image is 32-bit or 64-bit floating-point, the pixel values are multiplied by 255. 
       That is, the value range [0,1] is mapped to [0,255].
    ☯ If window was created with OpenGL support, 
       cv::imshow also support ogl::Buffer , ogl::Texture2D and cuda::GpuMat as input.
If the window was not created before this function, it is assumed creating a window with cv::WINDOW_AUTOSIZE.
If you need to show an image that is bigger than the screen resolution, 
you will need to call namedWindow("", WINDOW_NORMAL) before the imshow.

[Windows Backend Only] Pressing Ctrl+C will copy the image to the clipboard.
[Windows Backend Only] Pressing Ctrl+S will show a dialog to save the image.
'''
cv.imshow(winname, mat)

###########################################################################################
# 获取客户去矩形
###########################################################################################
# Provides rectangle of image in the window.
# retval = cv.getWindowImageRect(winname)
# The function getWindowImageRect returns the client screen coordinates, 
# width and height of the image rendering area.
retval = cv.getWindowImageRect(winname)
print("getWindowImageRect", retval)

###########################################################################################
# 获取窗口属性
###########################################################################################
# Provides parameters of a window.
# retval = cv.getWindowProperty(winname, prop_id)
# The function getWindowProperty returns properties of a window.
'''
Parameters
    winname Name of the window.
    prop_id Window property to retrieve. The following operation flags are available: (cv::WindowPropertyFlags)
'''
# WindowPropertyFlags
'''
cv.WND_PROP_FULLSCREEN
    fullscreen property (can be WINDOW_NORMAL or WINDOW_FULLSCREEN).

cv.WND_PROP_AUTOSIZE
    autosize property (can be WINDOW_NORMAL or WINDOW_AUTOSIZE).

cv.WND_PROP_ASPECT_RATIO
    window's aspect ration (can be set to WINDOW_FREERATIO or WINDOW_KEEPRATIO).

cv.WND_PROP_OPENGL
    opengl support.

cv.WND_PROP_VISIBLE
    checks whether the window exists and is visible

cv.WND_PROP_TOPMOST
    property to toggle normal window being topmost or not
'''
print("cv.WND_PROP_FULLSCREEN",   cv.getWindowProperty(winname, cv.WND_PROP_FULLSCREEN))
print("cv.WND_PROP_AUTOSIZE",     cv.getWindowProperty(winname, cv.WND_PROP_AUTOSIZE))
print("cv.WND_PROP_ASPECT_RATIO", cv.getWindowProperty(winname, cv.WND_PROP_ASPECT_RATIO))
print("cv.WND_PROP_OPENGL",       cv.getWindowProperty(winname, cv.WND_PROP_OPENGL))
print("cv.WND_PROP_VISIBLE",      cv.getWindowProperty(winname, cv.WND_PROP_VISIBLE))
print("cv.WND_PROP_TOPMOST",      cv.getWindowProperty(winname, cv.WND_PROP_TOPMOST))
cv.waitKey()

###########################################################################################
# 移动窗口
###########################################################################################
# Moves the window to the specified position.
# None = cv.moveWindow(winname, x, y)
'''
Parameters
    winname Name of the window.
    x       The new x-coordinate of the window.
    y       The new y-coordinate of the window.
'''
cv.moveWindow(winname, 200, 200)
cv.waitKey()

###########################################################################################
# 设置窗口尺寸
###########################################################################################
# Resizes the window to the specified size.
# None = cv.resizeWindow(winname, width, height)
# None = cv.resizeWindow(winname, size)
'''
Parameters
    winname Window name.
    width   The new window width.
    height  The new window height.

The specified window size is for the image area. Toolbars are not counted.
Only windows created without cv::WINDOW_AUTOSIZE flag can be resized.
'''
cv.resizeWindow(winname, 800, 600)
cv.waitKey()

###########################################################################################
# 用鼠标绘制矩形ROI区域
###########################################################################################
# Allows users to select a ROI on the given image.
# retval = cv.selectROI(windowName, img[, showCrosshair[, fromCenter]])
# retval = cv.selectROI(img[, showCrosshair[, fromCenter]])
'''
The function creates a window and allows users to select a ROI using the mouse. 
Controls: use space or enter to finish selection, use key c to cancel selection (function will return the zero cv::Rect).

Parameters
    windowName      name of the window where selection process will be shown.
    img             image to select a ROI.
    showCrosshair   if true crosshair of selection rectangle will be shown.
    fromCenter      if true center of selection will match initial mouse position. 
                    In opposite case a corner of selection rectangle will correspont to the initial mouse position.
Returns
    selected ROI or empty rect if selection canceled.
'''
retval = cv.selectROI(winname, mat, True, True)
print(retval)
###########################################################################################
# 用鼠标绘制多个矩形ROI区域
###########################################################################################
# Selects ROIs on the given image. Function creates a window and allows user to select a ROIs using mouse.
# Controls: use space or enter to finish current selection and start a new one,
# use esc to terminate multiple ROI selection process.
# boundingBoxes=cv.selectROIs(windowName, img[, showCrosshair[, fromCenter]])
'''
Parameters
    windowName      name of the window where selection process will be shown.
    img             image to select a ROI.
    boundingBoxes   selected ROIs.
    showCrosshair   if true crosshair of selection rectangle will be shown.
    fromCenter      if true center of selection will match initial mouse position.
                    In opposite case a corner of selection rectangle will correspont to the initial mouse position.
'''
boundingBoxes=cv.selectROIs(winname, mat, True, True)
print(boundingBoxes)

###########################################################################################
# 等待按键
###########################################################################################
# Waits for a pressed key.
# retval = cv.waitKey([, delay])
# The function waitKey waits for a key event infinitely (when delay≤0 ) or for delay milliseconds,
# when it is positive. Since the OS has a minimum time between switching threads, 
# the function will not wait exactly delay ms, it will wait at least delay ms, 
# depending on what else is running on your computer at that time. 
# It returns the code of the pressed key or -1 if no key was pressed before the specified time had elapsed.
'''
Parameters
    delay   Delay in milliseconds. 0 is the special value that means "forever".
'''
'''
This function is the only method in HighGUI that can fetch and handle events, 
so it needs to be called periodically for normal event processing
unless HighGUI is used within an environment that takes care of event processing.

The function only works if there is at least one HighGUI window created and the window is active. 
If there are several HighGUI windows, any of them can be active.
'''
retval = cv.waitKey()
print(retval)

# Similar to waitKey, but returns full key code.
# retval = cv.waitKeyEx([, delay])
'''
Key code is implementation specific and depends on used backend: QT/GTK/Win32/etc
'''
retval = cv.waitKeyEx()
print(retval)

###########################################################################################
# 销毁指定窗口
###########################################################################################
# Destroys the specified window.
# None = cv.destroyWindow(winname)
# The function destroyWindow destroys the window with the given name.
'''
Parameters
    winname	Name of the window to be destroyed.
'''
cv.destroyWindow(winname)

###########################################################################################
# 销毁所有窗口
###########################################################################################
# Destroys all of the HighGUI windows.
# None = cv.destroyAllWindows()
# The function destroyAllWindows destroys all of the opened HighGUI windows.
cv.destroyAllWindows()


