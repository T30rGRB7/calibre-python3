# vim:fileencoding=utf-8
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)
__license__   = 'GPL v3'
__copyright__ = '2013, Jellby <jellby at yahoo.com>'
'''
Write a t4b file to disk.
'''

from io import BytesIO

DEFAULT_T4B_DATA = b'\x74\x34\x62\x70\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc4\x00\x16\xdf\xff\xff\xf7\x6d\xff\xff\xfd\x7a\xff\xff\xff\xe7\x77\x76\xff\xf6\x77\x77\x8d\xff\xff\xe7\x77\x78\xbf\xff\xff\xf7\x77\x77\x77\x7d\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe4\x03\x78\x61\x07\xff\xff\x90\x04\xff\xff\xfc\x05\xff\xff\xff\xd5\x30\x35\xff\xf0\x13\x32\x00\x5f\xff\xd0\x03\x32\x01\xbf\xff\xe0\x00\x00\x00\x0b\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x50\x8f\xff\xff\x75\xff\xff\x40\x30\xef\xff\xfc\x06\xff\xff\xff\xff\xa0\x9f\xff\xf0\x6f\xff\xf5\x0d\xff\xd0\x4f\xff\xd0\x0f\xff\xe0\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfd\x05\xff\xff\xff\xfe\xff\xfe\x03\xa0\x8f\xff\xfc\x06\xff\xff\xff\xff\xa0\x9f\xff\xf0\x6f\xff\xfb\x0b\xff\xd0\x4f\xff\xf7\x0d\xff\xe0\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf6\x0e\xff\xff\xff\xff\xff\xfa\x0b\xe0\x3f\xff\xfc\x06\xff\xff\xff\xff\xa0\x9f\xff\xf0\x6f\xff\xf5\x0e\xff\xd0\x4f\xff\xf8\x0e\xff\xe0\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf1\x1f\xff\xff\xff\xff\xff\xf2\x0f\xf3\x0d\xff\xfc\x06\xff\xff\xff\xff\xa0\x9f\xff\xf0\x39\x88\x30\xaf\xff\xd0\x4f\xff\xf2\x1f\xff\xe0\x18\x88\x88\x8d\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf0\x3f\xff\xff\xff\xff\xff\xd0\x6f\xfc\x09\xff\xfc\x06\xff\xff\xff\xff\xa0\x9f\xff\xf0\x01\x11\x00\x2c\xff\xd0\x3a\xa8\x20\xcf\xff\xe0\x00\x00\x00\x0b\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf0\x2f\xff\xff\xff\xff\xff\x60\xaf\xff\x11\xff\xfc\x06\xff\xff\xff\xff\xa0\x9f\xff\xf0\x6f\xff\xfd\x10\xef\xd0\x00\x00\x1e\xff\xff\xe0\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf2\x0f\xff\xff\xff\xff\xfe\x20\x12\x22\x00\xcf\xfc\x06\xff\xff\xff\xff\xa0\x9f\xff\xf0\x6f\xff\xff\x90\x9f\xd0\x3d\xd8\x09\xff\xff\xe0\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf8\x0b\xff\xff\xff\xff\xfc\x03\x88\x88\x60\x4f\xfc\x06\xff\xff\xff\xff\xa0\x9f\xff\xf0\x6f\xff\xff\xa0\x8f\xd0\x4f\xff\x40\xcf\xff\xe0\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\xef\xff\xff\xfb\xf7\x0d\xff\xff\xf1\x1e\xfc\x06\xff\xff\xff\xff\xa0\x9f\xff\xf0\x6f\xff\xff\x60\xcf\xd0\x4f\xff\xf3\x0d\xff\xe0\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x80\x2c\xff\xfa\x05\xf0\x2f\xff\xff\xf6\x0b\xfc\x03\x88\x88\x88\xff\xb0\xaf\xff\xf0\x5d\xcc\xa3\x05\xff\xd0\x4f\xff\xfe\x11\xef\xe0\x18\x88\x88\x8d\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf8\x10\x01\x00\x3b\xb0\x9f\xff\xff\xfd\x06\xfc\x00\x00\x00\x00\xd0\x00\x00\xff\xf0\x00\x00\x02\x7f\xff\xe1\x5f\xff\xff\xc0\x5f\xe1\x00\x00\x00\x0b\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xed\xa9\xbd\xff\xed\xff\xff\xff\xff\xde\xff\xdd\xdd\xdd\xdd\xfd\xdd\xdd\xff\xfd\xdd\xdd\xee\xff\xff\xfd\xef\xff\xff\xfe\xdf\xfd\xdd\xdd\xdd\xdf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xed\xdb\x86\x8e\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xb7\x42\x00\x00\x0b\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfd\x00\x00\x00\x00\x09\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfd\x00\x00\x01\x11\x17\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xee\xee\xee\xee\xee\xee\xee\xee\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\x22\x45\x78\x9b\x95\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xb8\x77\x78\x88\x88\x88\x87\x87\x89\xdf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\x57\x9a\xaa\xaa\x94\xdf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfb\x00\x00\x11\x11\x22\x12\x11\x11\x10\x7e\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x76\xaa\xaa\xab\xa4\xcf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x12\x23\x33\x33\x33\x33\x32\x21\x6e\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xa5\xaa\xa9\x99\xa5\xaf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x33\x44\x44\x44\x33\x21\x6d\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xb4\xaa\xa9\xa9\xb6\x8f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x23\x34\x44\x54\x55\x44\x44\x31\x6d\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc5\x9a\x99\x9a\xb8\x7e\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x23\x34\x44\x44\x55\x45\x44\x31\x6d\xff\xff\xff\xff\xff\xff\xff\xff\xee\xdd\xdd\xee\xee\xc5\x9a\x88\x8a\xa9\x6e\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x44\x44\x44\x44\x44\x31\x6d\xff\xff\xff\xff\xff\xff\xff\xfe\xdc\xbb\xab\xcc\xca\x84\x8a\xa9\x99\xaa\x5d\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x44\x44\x44\x44\x44\x31\x6d\xff\xff\xff\xff\xff\xff\xff\xed\xa9\x99\x78\x87\x78\x84\x7a\xaa\x89\x9a\x6c\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x23\x34\x44\x45\x55\x55\x44\x31\x6d\xff\xff\xff\xff\xff\xff\xff\xec\x98\x88\x76\x98\x88\x74\x7a\xaa\xa7\x9a\x6b\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x23\x33\x34\x44\x54\x44\x44\x31\x6d\xff\xff\xff\xff\xff\xff\xff\xdb\x98\x88\x76\x98\x88\x74\x5a\xaa\x89\x9b\x7a\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x44\x45\x55\x54\x43\x31\x6d\xff\xff\xff\xff\xff\xff\xfe\xdb\x98\x88\x76\x98\x88\x84\x4a\xaa\x97\xbb\x79\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x34\x44\x44\x44\x44\x31\x5b\xcc\xcc\xcc\xcc\xcc\xcc\xcb\xba\x98\x88\x76\x88\x88\x85\x39\xa9\x8a\xab\x97\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x33\x34\x44\x44\x43\x31\x34\x44\x44\x55\x55\x55\x55\x44\x46\x98\x88\x76\x78\x88\x85\x28\xa8\x9a\xab\xa5\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf9\x00\x11\x11\x11\x12\x22\x22\x11\x10\x00\x01\x22\x23\x33\x33\x33\x31\x11\x88\x88\x76\x68\x88\x85\x27\xa9\xa9\xab\xa5\xdf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x12\x23\x33\x33\x44\x43\x33\x21\x00\x12\x33\x44\x55\x55\x65\x42\x11\x78\x88\x76\x68\x88\x85\x36\xaa\xaa\xab\xb5\xcf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x34\x44\x54\x44\x44\x21\x01\x23\x44\x55\x66\x66\x66\x53\x21\x78\x88\x86\x68\x88\x85\x45\xaa\xaa\xbb\xb6\xaf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x34\x44\x44\x44\x33\x21\x01\x23\x45\x56\x67\x77\x77\x54\x21\x78\x88\x86\x68\x88\x85\x54\xaa\xab\xbb\xb7\x8f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x44\x44\x44\x44\x43\x21\x01\x23\x57\x8a\xaa\xaa\x99\x74\x21\x79\x88\x86\x68\x88\x75\x44\x9a\xab\xbb\xb9\x6e\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x34\x44\x44\x55\x43\x21\x01\x24\x56\x78\x89\x99\x88\x74\x21\x69\x88\x87\x68\x88\x75\x53\x9a\xab\xbb\xba\x5e\xff\xff\xff\xff\xff\xed\xa7\x9e\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x44\x34\x44\x54\x44\x21\x01\x23\x45\x56\x67\x77\x77\x64\x21\x69\x88\x87\x68\x88\x65\x53\x8a\xaa\xaa\xba\x5d\xff\xff\xff\xed\xb9\x75\x54\x5b\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x84\x66\x48\x54\x43\x21\x01\x23\x45\x56\x67\x77\x76\x64\x21\x6a\x88\x87\x68\x88\x66\x54\x7a\xaa\x9a\xbb\x6b\xff\xee\xb9\x66\x66\x78\x75\x69\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x64\x54\x47\x54\x43\x21\x01\x23\x45\x66\x77\x67\x67\x64\x21\x6a\x88\x87\x68\x88\x76\x54\x6a\xbb\xba\xbb\x79\xca\x75\x56\x77\x88\x88\x85\x68\xef\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x23\x33\xba\xba\xac\x44\x43\x21\x01\x23\x45\x56\x66\x66\x76\x64\x21\x6a\x88\x87\x67\x88\x66\x54\x5a\xbb\xa9\xbb\x83\x45\x67\x78\x64\x78\x88\x86\x66\xdf\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x87\x77\x79\x54\x43\x21\x01\x23\x45\x56\x66\x67\x77\x54\x21\x6a\x88\x87\x67\x88\x66\x54\x4a\xbb\xab\xbb\x93\x47\x88\x88\x66\x38\x88\x98\x66\xbf\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x44\x44\x44\x54\x44\x21\x01\x23\x45\x56\x66\x67\x77\x64\x21\x6a\x88\x88\x66\x98\x66\x55\x3a\xab\xba\xab\xa4\x47\x88\x87\x68\x43\x89\x99\x57\x8f\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x32\x34\x3a\x44\x43\x21\x01\x23\x45\x56\x66\x67\x66\x64\x31\x69\x88\x88\x65\x98\x66\x55\x39\xbb\xba\xbc\xa4\x47\x88\x87\x77\x85\x37\xaa\x78\x7e\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\xad\x76\xc5\x44\x33\x21\x01\x23\x44\x56\x66\x77\x76\x54\x21\x69\x98\x88\x65\x98\x66\x65\x38\xbb\xb9\xbb\xb5\x46\x77\x86\x68\x87\x78\x9a\x87\x7c\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x84\x7b\x44\x44\x33\x21\x01\x23\x44\x56\x67\x76\x76\x63\x21\x79\x98\x88\x76\x87\x66\x65\x46\xaa\x99\xab\xb5\x45\x88\x76\x67\x77\x78\x9a\x96\x8a\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x63\x54\x46\x54\x43\x21\x01\x23\x44\x55\x66\x67\x76\x64\x21\x79\x98\x88\x76\x77\x66\x65\x44\xab\xbb\xaa\xb7\x35\x88\x87\x77\x89\x99\x9a\x96\x89\xef\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\xbb\xba\xbc\x44\x43\x21\x01\x23\x44\x56\x67\x66\x76\x63\x21\x79\x98\x88\x76\x68\x66\x65\x53\xab\xba\xaa\xb8\x35\x78\x88\x89\x99\x99\x9a\xa7\x88\xef\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x54\x44\x45\x44\x34\x21\x01\x23\x44\x56\x66\x86\x66\x54\x21\x79\x98\x88\x76\x68\x66\x65\x63\x9a\xba\xab\xb9\x35\x68\x88\x99\x99\x9a\x9a\xa8\x77\xcf\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x33\x43\x43\x44\x43\x21\x01\x23\x44\x55\x66\x76\x66\x54\x21\x7a\x98\x88\x76\x68\x66\x65\x63\x8a\xab\xa9\xba\x35\x58\x88\x99\x99\x99\x9a\xa9\x67\xaf\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x12\x23\x69\x2a\xd9\x34\x33\x21\x01\x23\x44\x55\x67\x67\x66\x53\x21\x7a\x98\x88\x76\x67\x66\x66\x54\x7a\xa9\x9a\xbb\x44\x48\x99\x99\x89\x99\xaa\xaa\x68\x8e\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x97\x98\x47\x44\x34\x21\x01\x23\x44\x56\x66\x76\x66\x53\x21\x7a\x98\x88\x76\x67\x66\x66\x55\x6a\xbb\x9a\xbb\x54\x57\x99\x98\x79\x9a\xaa\xaa\x87\x7d\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x53\x44\x36\x54\x44\x21\x00\x23\x44\x55\x66\x66\x66\x53\x21\x7a\x98\x87\x76\x67\x66\x66\x55\x5a\xaa\xaa\xbb\x73\x66\x99\x66\x59\x77\xaa\xaa\x97\x8b\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\xcc\xcc\xcd\x44\x33\x21\x01\x23\x34\x55\x66\x66\x66\x53\x21\x7b\x98\x88\x76\x66\x66\x66\x65\x4a\xaa\xab\xab\x83\x66\x88\x55\x48\x84\x5a\xaa\xa6\x89\xff\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x44\x34\x45\x44\x33\x21\x01\x23\x44\x55\x56\x66\x66\x53\x21\x7b\x98\x88\x76\x66\x66\x66\x56\x49\x9a\xaa\x9b\x94\x55\x88\x66\x78\x86\x98\xaa\xa7\x88\xef\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x33\x33\x44\x44\x33\x21\x00\x22\x34\x55\x66\x66\x66\x53\x21\x8b\xa7\x88\x86\x66\x66\x66\x56\x38\xa7\x99\xaa\x95\x56\x79\x99\x97\x76\x96\xaa\xa8\x88\xdf\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x33\x76\x77\x78\x44\x33\x21\x01\x22\x34\x45\x54\x66\x66\x53\x21\x8b\xa7\x78\x86\x56\x66\x66\x55\x48\xaa\xaa\xaa\xa5\x56\x69\x99\x99\x85\x79\x7a\xa9\x68\xbf\xff\xff\xff\xff\xff\xff\xfa\x11\x12\x33\xaa\xaa\xab\x34\x33\x21\x00\x23\x34\x45\x6b\x66\x66\x53\x21\x8b\xa8\x78\x76\x56\x76\x66\x65\x47\xaa\xa9\x9a\xa6\x66\x59\x99\x99\xa6\x6a\x6a\xaa\x68\x9f\xff\xff\xff\xff\xff\xff\xfa\x11\x12\x23\x43\x33\x33\x34\x33\x21\x00\x22\x34\x45\x68\x86\x66\x53\x21\x8c\xa8\x77\x76\x56\x76\x66\x66\x45\xaa\xa9\xab\xb6\x85\x58\x99\x99\x99\x6a\x69\xaa\x67\x7e\xff\xff\xff\xff\xff\xff\xfa\x11\x12\x23\x33\x34\x49\x75\x33\x21\x00\x22\x34\x45\x66\x66\x65\x53\x21\x8c\xa8\x77\x66\x55\x76\x66\x66\x54\xa9\x99\x9b\xa7\x76\x66\x99\x99\xa6\x69\x88\xaa\x87\x6c\xff\xff\xff\xff\xff\xff\xfa\x11\x12\x23\x33\x33\x37\x34\x33\x21\x00\x12\x34\x45\x59\x86\x66\x53\x21\x8c\xb9\x77\x66\x55\x76\x66\x65\x63\x9a\xaa\xba\xb8\x67\x66\x99\x99\x97\x68\x96\xaa\xa6\x7a\xff\xff\xff\xff\xff\xff\xfa\x11\x22\x23\x54\x44\x46\x44\x43\x21\x00\x22\x34\x58\x59\xa5\x65\x53\x21\x8c\xb9\x77\x76\x56\x76\x66\x65\x63\x8a\xaa\xaa\xb9\x58\x65\x89\x99\x99\x86\xa3\xaa\xa6\x88\xef\xff\xff\xff\xff\xff\xfa\x11\x12\x23\xab\xbb\xbc\x33\x33\x21\x00\x12\x34\x46\x66\x66\x55\x43\x21\x8c\xb9\x77\x76\x56\x76\x66\x65\x64\x7a\xaa\x9a\xba\x49\x66\x89\x99\x99\x95\xa4\x5a\xa7\x87\xdf\xff\xff\xff\xff\xff\xfa\x11\x12\x22\x42\x33\x35\x44\x33\x21\x00\x12\x34\x48\x86\x85\x55\x43\x21\x8c\xb9\x67\x77\x56\x67\x66\x66\x65\x6a\xaa\x9a\xba\x4a\x67\x79\x99\x86\x76\x86\x27\xa8\x67\xcf\xff\xff\xff\xff\xff\xfa\x11\x12\x23\x33\x33\x35\x33\x33\x21\x00\x12\x33\x54\x88\x56\x65\x43\x21\x8d\xba\x66\x77\x56\x57\x66\x66\x65\x5a\xab\xaa\xbb\x59\x76\x59\x99\x99\x97\x98\x24\xa9\x67\xaf\xff\xff\xff\xff\xff\xfa\x11\x12\x22\x21\x36\x9b\x33\x33\x21\x00\x12\x34\x45\x56\x76\x55\x43\x21\x8d\xca\x76\x77\x66\x57\x66\x65\x65\x5a\xaa\x9a\xbb\x78\x96\x58\x99\x99\x88\x9a\x44\xa9\x67\x8e\xff\xff\xff\xff\xff\xfa\x11\x12\x23\x6a\xb7\x44\x43\x33\x21\x00\x12\x34\x44\x55\x85\x55\x43\x21\x8d\xca\x77\x67\x66\x67\x66\x66\x66\x49\xaa\xaa\xab\x87\xc5\x57\x98\x98\x87\x68\x85\x99\x76\x6d\xff\xff\xff\xff\xff\xfa\x11\x12\x23\x96\x33\x43\x33\x33\x21\x00\x12\x33\x44\x65\x55\x55\x43\x21\x8d\xca\x87\x76\x66\x67\x66\x66\x56\x59\xa9\x99\xab\x96\xc6\x65\x98\x89\x99\x68\x98\x99\x86\x6b\xff\xff\xff\xff\xff\xfa\x11\x12\x22\x44\x75\x23\x33\x33\x21\x00\x12\x33\x44\x6a\x65\x55\x43\x21\x8d\xca\x87\x76\x66\x67\x66\x66\x66\x58\xa8\x9a\x9b\xa5\xc9\x65\x88\x89\x99\x77\x98\x99\x95\x68\xff\xff\xff\xff\xff\xfa\x11\x12\x22\x22\x24\x79\x33\x33\x21\x00\x12\x34\x44\x56\x75\x55\x43\x21\x8d\xda\x87\x77\x66\x67\x66\x66\x66\x47\xa9\x9a\xbb\xa6\xcb\x65\x78\x88\x88\x85\x68\x99\x96\x66\xef\xff\xff\xff\xff\xfa\x11\x12\x23\x11\x33\x34\x33\x32\x21\x00\x12\x33\x44\x57\x65\x55\x43\x21\x8d\xda\x87\x77\x65\x76\x76\x66\x67\x56\xaa\xbb\xaa\xa6\xbc\x66\x68\x88\x88\x85\x88\x89\x97\x66\xcf\xff\xff\xff\xff\xfa\x11\x12\x23\x95\x23\x36\x33\x33\x21\x00\x12\x33\x44\x58\x65\x55\x43\x21\x8d\xda\x96\x77\x65\x77\x66\x66\x57\x55\xaa\xaa\xaa\xb6\xad\x66\x58\x88\x88\x85\x78\x88\x98\x66\xaf\xff\xff\xff\xff\xfa\x11\x12\x22\x52\x33\x35\x33\x33\x21\x00\x12\x33\x44\x55\x65\x55\x42\x21\x8e\xdb\x97\x67\x75\x77\x66\x66\x56\x64\xaa\xbb\xaa\xa7\x8e\x85\x58\x87\x88\x87\x88\x88\x88\x56\x8f\xff\xff\xff\xff\xfa\x11\x12\x22\x42\x23\x35\x43\x32\x21\x00\x12\x33\x44\x48\x85\x55\x43\x21\x8e\xdb\x97\x67\x75\x77\x66\x66\x66\x73\x9b\xaa\xaa\xb8\x6e\xb4\x57\x87\x87\x77\x78\x88\x88\x56\x7e\xff\xff\xff\xff\xfa\x11\x12\x22\x42\x33\x28\x33\x32\x21\x00\x12\x33\x44\x55\x55\x55\x43\x21\x8e\xdb\x97\x76\x76\x67\x76\x66\x66\x74\x8a\xba\xaa\xb9\x5d\xd5\x55\x77\x77\x77\x47\x88\x88\x65\x5d\xff\xff\xff\xff\xfa\x10\x12\x22\x63\x11\x78\x33\x32\x20\x00\x12\x33\x34\x47\x84\x55\x42\x21\x8e\xec\x97\x77\x66\x67\x87\x76\x66\x74\x7a\xaa\xaa\xba\x4d\xe7\x54\x77\x77\x77\x56\x87\x88\x74\x5a\xff\xff\xff\xff\xfa\x11\x12\x22\x28\x9a\x83\x33\x32\x20\x00\x12\x33\x44\x55\x55\x55\x42\x21\x9e\xec\x97\x77\x66\x67\x76\x66\x66\x76\x6a\xaa\x99\xba\x4b\xfa\x54\x67\x77\x77\x65\x77\x77\x84\x57\xef\xff\xff\xff\xfa\x11\x12\x22\x22\x33\x33\x33\x22\x10\x00\x12\x33\x33\x56\x45\x54\x42\x11\x9e\xec\x97\x77\x75\x67\x76\x66\x65\x67\x5a\xaa\x99\xba\x59\xfc\x54\x57\x77\x76\x65\x77\x77\x75\x55\xdf\xff\xff\xff\xfa\x11\x12\x22\x22\x33\x33\x33\x22\x20\x00\x12\x33\x35\x45\x65\x54\x42\x21\x9e\xec\xa7\x77\x76\x67\x86\x66\x65\x68\x4a\xa9\x8a\xbb\x77\xfd\x65\x56\x76\x76\x64\x67\x77\x76\x55\xbf\xff\xff\xff\xfa\x11\x12\x22\x22\x32\x33\x23\x22\x20\x00\x12\x23\x45\x55\x54\x44\x42\x11\x9e\xec\xa7\x67\x76\x68\x77\x66\x66\x68\x4a\xb9\x88\xaa\x96\xef\x75\x46\x66\x66\x65\x45\x77\x77\x45\x9f\xff\xff\xff\xfa\x10\x12\x22\x22\x22\x33\x32\x22\x20\x00\x12\x23\x33\x44\x54\x54\x42\x21\x8e\xed\xa8\x76\x76\x58\x77\x66\x66\x67\x59\xba\xa8\xa9\xa5\xef\x94\x46\x66\x66\x66\x46\x67\x77\x45\x7e\xff\xff\xff\xfa\x11\x12\x22\x22\x33\x33\x23\x32\x21\x00\x12\x23\x34\x54\x44\x44\x42\x11\x8e\xfd\xb8\x76\x67\x67\x68\x77\x66\x67\x68\xaa\xa9\x7b\xa5\xcf\xc3\x45\x66\x66\x66\x67\x66\x67\x55\x5d\xff\xff\xff\xf9\x00\x00\x11\x11\x11\x11\x11\x11\x10\x00\x12\x23\x34\x34\x44\x44\x42\x11\x8e\xfd\xb8\x77\x66\x67\x77\x66\x66\x67\x77\xaa\xa8\xa9\xb6\xbf\xe5\x44\x66\x66\x66\x66\x66\x67\x54\x4b\xff\xff\xff\xf9\x00\x01\x11\x11\x11\x11\x11\x11\x10\x00\x12\x23\x33\x44\x44\x44\x32\x11\x8e\xfd\xb8\x77\x76\x67\x77\x66\x66\x57\x76\xba\xa8\x7a\xb6\xaf\xf8\x43\x66\x66\x66\x66\x66\x66\x63\x48\xff\xff\xff\xfa\x10\x11\x22\x22\x22\x22\x32\x22\x10\x00\x12\x23\x34\x44\x44\x44\x32\x11\x8e\xfd\xb9\x77\x76\x57\x87\x66\x66\x66\x85\xbb\xa8\x8b\xa7\x9f\xfb\x43\x56\x66\x66\x66\x66\x66\x64\x45\xef\xff\xff\xfa\x10\x12\x22\x22\x22\x32\x22\x22\x10\x00\x12\x23\x33\x44\x44\x44\x32\x11\x8e\xfe\xb9\x67\x77\x57\x87\x76\x66\x66\x84\xab\x89\xaa\xb8\x8e\xfd\x54\x46\x66\x55\x55\x55\x66\x65\x43\xdf\xff\xff\xfa\x10\x12\x22\x22\x22\x32\x22\x22\x20\x00\x12\x23\x33\x44\x44\x44\x32\x11\x8e\xfe\xca\x66\x77\x57\x87\x77\x66\x67\x84\xab\x9a\xa9\xb9\x6e\xfe\x64\x35\x66\x55\x66\x65\x56\x66\x34\x9f\xff\xff\xfa\x10\x11\x12\x22\x22\x33\x22\x22\x10\x00\x11\x23\x34\x44\x55\x44\x32\x11\x8e\xfe\xca\x76\x77\x66\x87\x76\x66\x57\x84\x9b\x9a\x9a\xaa\x5d\xff\x84\x35\x66\x56\x66\x55\x45\x66\x44\x7f\xff\xff\xfa\x00\x11\x22\x22\x22\x22\x32\x22\x10\x00\x12\x34\x67\x78\x88\x76\x53\x11\x8e\xfe\xca\x76\x67\x66\x88\x66\x66\x56\x85\x7b\xaa\xba\xaa\x4c\xff\xb4\x45\x66\x55\x55\x45\x45\x66\x44\x5d\xff\xff\xfa\x10\x11\x22\x22\x33\x33\x23\x32\x10\x00\x12\x23\x34\x44\x44\x44\x42\x11\x8e\xfe\xca\x77\x66\x66\x88\x66\x66\x66\x87\x6b\xba\xab\xbb\x4b\xff\xd4\x44\x65\x54\x44\x44\x45\x55\x43\x4c\xff\xff\xfa\x00\x11\x22\x22\x22\x22\x22\x22\x10\x00\x11\x22\x33\x34\x44\x44\x32\x11\x8d\xed\xb9\x87\x76\x66\x78\x76\x66\x66\x78\x4b\xba\x98\x65\x18\xff\xe6\x33\x55\x54\x44\x55\x55\x54\x42\x5d\xff\xff\xea\x00\x11\x11\x22\x22\x22\x22\x21\x10\x00\x11\x12\x22\x22\x33\x32\x21\x10\x6a\xba\x98\x87\x77\x66\x66\x77\x76\x66\x77\x23\x11\x11\x11\x05\xcd\xd8\x33\x55\x55\x55\x54\x44\x34\x7b\xdf\xee\xee\xd8\x00\x01\x11\x11\x11\x11\x11\x11\x00\x00\x00\x11\x11\x12\x22\x12\x11\x00\x59\x99\x87\x87\x77\x66\x66\x76\x76\x66\x77\x10\x11\x11\x11\x02\xaa\xa9\x33\x45\x55\x44\x44\x58\xbd\xee\xff\xdd\xcc\xb8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x11\x11\x11\x10\x00\x69\x99\x87\x97\x77\x76\x76\x76\x65\x55\x67\x20\x10\x00\x00\x05\x99\x98\x43\x24\x33\x46\x89\xbc\xcd\xde\xee\xdc\xcc\xba\x42\x22\x22\x22\x22\x22\x22\x22\x22\x42\x11\x22\x22\x22\x22\x22\x21\x24\x79\x99\x88\x97\x66\x77\x77\x86\x67\x77\x88\x50\x00\x23\x46\x88\x99\x99\x63\x25\x78\x9a\xab\xbc\xcd\xde\xee\xee\xed\xdc\xbb\xaa\xa9\x99\x99\x99\x88\x88\x88\x88\x77\x77\x77\x77\x77\x77\x77\x78\x99\x99\x98\x88\x88\x88\x88\x88\x88\x88\x99\x87\x78\x99\x99\xaa\xaa\xaa\xa9\xaa\xbb\xcc\xcd\xdd\xee\xef\xff\xff\xff\xff\xee\xee\xed\xdd\xdd\xdc\xcc\xcc\xcc\xbb\xbb\xbb\xbb\xbb\xbb\xba\xaa\xaa\xab\xba\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xbb\xbb\xbb\xbb\xcc\xcc\xcc\xcd\xdd\xdd\xde\xee\xee\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xed\xdd\xdd\xdd\xee\xee\xee\xee\xee\xee\xee\xee\xee\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'  # noqa


def reduce_color(c):
    return max(0, min(255, c))//16


def write_t4b(t4bfile, coverdata=None):
    '''
    t4bfile is a file handle ready to write binary data to disk.
    coverdata is a string representation of a JPEG file.
    '''
    from PIL import Image
    if coverdata is not None:
        coverdata = BytesIO(coverdata)
        cover = Image.open(coverdata).convert("L")
        cover.thumbnail((96, 144), Image.ANTIALIAS)
        t4bcover = Image.new('L', (96, 144), 'white')

        x, y = cover.size
        t4bcover.paste(cover, ((96-x)//2, (144-y)//2))

        pxs = t4bcover.getdata()
        t4bfile.write(b't4bp')
        data = (16 * reduce_color(pxs[i]) + reduce_color(pxs[i+1])
                          for i in range(0, len(pxs), 2))
        t4bfile.write(bytes(bytearray(data)))
    else:
        t4bfile.write(DEFAULT_T4B_DATA)

