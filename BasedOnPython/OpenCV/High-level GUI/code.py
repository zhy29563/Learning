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
    state	    current state of the button. It could be -1 for a push button, 0 or 1 for a check/radio box button.
    userdata	The optional parameter.
'''

# MouseCallback
# Callback function for mouse events. see cv::setMouseCallback.
# typedef void(* cv::MouseCallback) (int event, int x, int y, int flags, void *userdata)
'''
Parameters
    event	    one of the cv::MouseEventTypes constants.
    x	        The x-coordinate of the mouse event.
    y	        The y-coordinate of the mouse event.
    flags	    one of the cv::MouseEventFlags constants.
    userdata	The optional parameter.
'''

# OpenGlDrawCallback
# Callback function defined to be called every frame. See cv::setOpenGlDrawCallback.
# typedef void(* cv::OpenGlDrawCallback) (void *userdata)
'''
Parameters
    userdata	The optional parameter.
'''

# TrackbarCallback
# Callback function for Trackbar see cv::createTrackbar.
# typedef void(* cv::TrackbarCallback) (int pos, void *userdata)
'''
Parameters
    pos	        current position of the specified trackbar.
    userdata	The optional parameter.
'''
import numpy as np
import cv2 as cv

# Creates a window.
# None	=	cv.namedWindow(	winname[, flags]	)
# The function namedWindow creates a window that can be used as a placeholder for images and trackbars. 
# Created windows are referred to by their names.
# 
# If a window with the same name already exists, the function does nothing.
# 
# You can call cv::destroyWindow or cv::destroyAllWindows to close the window and de-allocate any associated memory usage.
# For a simple program, you do not really have to call these functions because all the resources and windows of the application are closed automatically by the operating system upon exit.
'''
Parameters
    winname	Name of the window in the window caption that may be used as a window identifier.
    flags	Flags of the window. The supported flags are: (cv::WindowFlags)
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
cv.namedWindow(winname, cv.WINDOW_GUI_EXPANDED|cv.WINDOW_NORMAL|cv.WINDOW_KEEPRATIO)

mat = cv.imread('lena.png')

# Updates window title.
# None = cv.setWindowTitle(winname, title)
'''
Parameters
    winname	Name of the window.
    title	New title.
'''
cv.setWindowTitle(winname, 'First OpenCV Window')
# Displays an image in the specified window.
# None	=	cv.imshow(	winname, mat	)
'''
Parameters
    winname	Name of the window.
    mat	    Image to be shown.
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

# Provides rectangle of image in the window.
# retval	=	cv.getWindowImageRect(	winname	)
# The function getWindowImageRect returns the client screen coordinates, width and height of the image rendering area.
retval	=	cv.getWindowImageRect(	winname	)
print("getWindowImageRect", retval)

# Provides parameters of a window.
# retval	=	cv.getWindowProperty(	winname, prop_id	)
# The function getWindowProperty returns properties of a window.
'''
Parameters
    winname	Name of the window.
    prop_id	Window property to retrieve. The following operation flags are available: (cv::WindowPropertyFlags)
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
print("cv.WND_PROP_FULLSCREEN", cv.getWindowProperty(winname, cv.WND_PROP_FULLSCREEN))
print("cv.WND_PROP_AUTOSIZE", cv.getWindowProperty(winname, cv.WND_PROP_AUTOSIZE))
print("cv.WND_PROP_ASPECT_RATIO", cv.getWindowProperty(winname, cv.WND_PROP_ASPECT_RATIO))
print("cv.WND_PROP_OPENGL", cv.getWindowProperty(winname, cv.WND_PROP_OPENGL))
print("cv.WND_PROP_VISIBLE", cv.getWindowProperty(winname, cv.WND_PROP_VISIBLE))
print("cv.WND_PROP_TOPMOST", cv.getWindowProperty(winname, cv.WND_PROP_TOPMOST))
cv.waitKey()

# Moves the window to the specified position.
# None	=	cv.moveWindow(	winname, x, y	)
'''
Parameters
    winname	Name of the window.
    x	    The new x-coordinate of the window.
    y	    The new y-coordinate of the window.
'''
cv.moveWindow(	winname, 200, 200)
cv.waitKey()

# Resizes the window to the specified size.
# None	=	cv.resizeWindow(	winname, width, height	)
# None	=	cv.resizeWindow(	winname, size	)
'''
Parameters
    winname	Window name.
    width	The new window width.
    height	The new window height.

The specified window size is for the image area. Toolbars are not counted.
Only windows created without cv::WINDOW_AUTOSIZE flag can be resized.
'''
cv.resizeWindow(winname, 200, 200)
cv.waitKey()

# Allows users to select a ROI on the given image.
# retval	=	cv.selectROI(	windowName, img[, showCrosshair[, fromCenter]]	)
# retval	=	cv.selectROI(	img[, showCrosshair[, fromCenter]]	)
'''
The function creates a window and allows users to select a ROI using the mouse. 
Controls: use space or enter to finish selection, use key c to cancel selection (function will return the zero cv::Rect).

Parameters
    windowName	    name of the window where selection process will be shown.
    img	            image to select a ROI.
    showCrosshair	if true crosshair of selection rectangle will be shown.
    fromCenter	    if true center of selection will match initial mouse position. 
                   In opposite case a corner of selection rectangle will correspont to the initial mouse position.
Returns
    selected ROI or empty rect if selection canceled.
'''
retval = cv.selectROI(	winname, mat, True, True)
print(retval)

# Waits for a pressed key.
# retval = cv.waitKey([, delay])
# The function waitKey waits for a key event infinitely (when delay≤0 ) or for delay milliseconds,
# when it is positive. Since the OS has a minimum time between switching threads, 
# the function will not wait exactly delay ms, it will wait at least delay ms, 
# depending on what else is running on your computer at that time. 
# It returns the code of the pressed key or -1 if no key was pressed before the specified time had elapsed.
'''
Parameters
    delay	Delay in milliseconds. 0 is the special value that means "forever".
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
# retval	=	cv.waitKeyEx(	[, delay]	)
'''
Key code is implementation specific and depends on used backend: QT/GTK/Win32/etc
'''
retval = cv.waitKeyEx()
print(retval)


# Destroys the specified window.
# None = cv.destroyWindow(winname)
# The function destroyWindow destroys the window with the given name.
'''
Parameters
    winname	Name of the window to be destroyed.
'''
cv.destroyWindow(winname)

# Destroys all of the HighGUI windows.
# None = cv.destroyAllWindows()
# The function destroyAllWindows destroys all of the opened HighGUI windows.
cv.destroyAllWindows()


