import struct

def check_pyc_version(filename):
    with open(filename, 'rb') as f:
        magic_number = f.read(4)
        # Unpack the first two bytes
        magic_int = struct.unpack('<H', magic_number[:2])[0]
        
        # Reference mapping for common recent versions
        versions = {
            3413: "3.12",
            3495: "3.11",
            3439: "3.10",
            3413: "3.9",
        }
        
        # 3.12 specifically usually starts with hex CB 0D
        if magic_number.startswith(b'\xcb\r\r\n'):
            return "Python 3.12"
        
        return f"Unknown Version (Magic: {magic_int})"

print(f"File version: {check_pyc_version('QuiG_Raman_Spectral_Analysis_Core.pyc')}")