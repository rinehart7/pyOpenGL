from OpenGL import GL as gl
import glfw

def setup():

    if not glfw.init():
        print("Failed to initialize glfw")
    
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    
    window = glfw.create_window(500, 300, "TITLE", None, None)
    glfw.make_context_current(window)
    glfw.swap_interval(0)
    gl.glClearColor(0, 0, 0.4, 0)
    
    return window