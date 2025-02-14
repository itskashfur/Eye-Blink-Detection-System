__all__: list[str] = []

# Enumerations
POINTS: int
LINES: int
LINE_LOOP: int
LINE_STRIP: int
TRIANGLES: int
TRIANGLE_STRIP: int
TRIANGLE_FAN: int
QUADS: int
QUAD_STRIP: int
POLYGON: int
RenderModes = int
"""One of [POINTS, LINES, LINE_LOOP, LINE_STRIP, TRIANGLES, TRIANGLE_STRIP, TRIANGLE_FAN, QUADS, QUAD_STRIP, POLYGON]"""


Buffer_ARRAY_BUFFER: int
BUFFER_ARRAY_BUFFER: int
Buffer_ELEMENT_ARRAY_BUFFER: int
BUFFER_ELEMENT_ARRAY_BUFFER: int
Buffer_PIXEL_PACK_BUFFER: int
BUFFER_PIXEL_PACK_BUFFER: int
Buffer_PIXEL_UNPACK_BUFFER: int
BUFFER_PIXEL_UNPACK_BUFFER: int
Buffer_Target = int
"""One of [Buffer_ARRAY_BUFFER, BUFFER_ARRAY_BUFFER, Buffer_ELEMENT_ARRAY_BUFFER, BUFFER_ELEMENT_ARRAY_BUFFER, Buffer_PIXEL_PACK_BUFFER, BUFFER_PIXEL_PACK_BUFFER, Buffer_PIXEL_UNPACK_BUFFER, BUFFER_PIXEL_UNPACK_BUFFER]"""

Buffer_READ_ONLY: int
BUFFER_READ_ONLY: int
Buffer_WRITE_ONLY: int
BUFFER_WRITE_ONLY: int
Buffer_READ_WRITE: int
BUFFER_READ_WRITE: int
Buffer_Access = int
"""One of [Buffer_READ_ONLY, BUFFER_READ_ONLY, Buffer_WRITE_ONLY, BUFFER_WRITE_ONLY, Buffer_READ_WRITE, BUFFER_READ_WRITE]"""

Texture2D_NONE: int
TEXTURE2D_NONE: int
Texture2D_DEPTH_COMPONENT: int
TEXTURE2D_DEPTH_COMPONENT: int
Texture2D_RGB: int
TEXTURE2D_RGB: int
Texture2D_RGBA: int
TEXTURE2D_RGBA: int
Texture2D_Format = int
"""One of [Texture2D_NONE, TEXTURE2D_NONE, Texture2D_DEPTH_COMPONENT, TEXTURE2D_DEPTH_COMPONENT, Texture2D_RGB, TEXTURE2D_RGB, Texture2D_RGBA, TEXTURE2D_RGBA]"""


# Classes

