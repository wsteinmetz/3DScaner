'''OpenGL extension ARB.copy_buffer

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_copy_buffer'
_DEPRECATED = False
GL_COPY_READ_BUFFER = constant.Constant( 'GL_COPY_READ_BUFFER', 0x8F36 )
GL_COPY_WRITE_BUFFER = constant.Constant( 'GL_COPY_WRITE_BUFFER', 0x8F37 )
glCopyBufferSubData = platform.createExtensionFunction( 
'glCopyBufferSubData',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLintptr,constants.GLintptr,constants.GLsizeiptr,),
doc='glCopyBufferSubData(GLenum(readTarget), GLenum(writeTarget), GLintptr(readOffset), GLintptr(writeOffset), GLsizeiptr(size)) -> None',
argNames=('readTarget','writeTarget','readOffset','writeOffset','size',),
deprecated=_DEPRECATED,
)


def glInitCopyBufferARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
