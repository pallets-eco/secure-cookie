import sys

PY2 = sys.version_info[0] == 2

if not PY2:
    text_type = str

    def to_bytes(x, charset=sys.getdefaultencoding(), errors="strict"):
        if x is None:
            return None

        if isinstance(x, (bytes, bytearray, memoryview)):
            return bytes(x)

        if isinstance(x, str):
            return x.encode(charset, errors)

        raise TypeError("Expected bytes")

    def to_native(x, charset=sys.getdefaultencoding(), errors="strict"):
        if x is None or isinstance(x, str):
            return x

        return x.decode(charset, errors)

else:
    text_type = unicode

    def to_bytes(x, encoding=sys.getdefaultencoding(), errors="strict"):
        if x is None:
            return None

        if isinstance(x, (bytes, bytearray, buffer)):
            return bytes(x)

        if isinstance(x, unicode):
            return x.encode(encoding, errors)

        raise TypeError("Expected bytes")

    def to_native(x, encoding=sys.getdefaultencoding(), errors="strict"):
        if x is None or isinstance(x, str):
            return x

        return x.encode(encoding, errors)
