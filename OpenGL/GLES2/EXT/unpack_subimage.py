'''OpenGL extension EXT.unpack_subimage

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.unpack_subimage to provide a more 
Python-friendly API

Overview (from the spec)
	
	This OpenGL ES 2.0 extension adds support for GL_UNPACK_ROW_LENGTH,
	GL_UNPACK_SKIP_ROWS and GL_UNPACK_SKIP_PIXELS as valid enums to
	PixelStore.  The functionality is the same as in OpenGL. These are
	useful for updating textures with a sub-rectangle of pixel data
	coming from a larger image in host memory.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/unpack_subimage.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.unpack_subimage import *
from OpenGL.raw.GLES2.EXT.unpack_subimage import _EXTENSION_NAME

def glInitUnpackSubimageEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION