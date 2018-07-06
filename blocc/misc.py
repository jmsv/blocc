def byte_me(thingy):
    if isinstance(thingy, bytes):
        return thingy

    return str(thingy).encode('utf-8')
