import string
import uuid


def base64uuid(fixed_length=0):
    uuid_int = uuid.uuid4().int
    chars = f"_{string.ascii_lowercase}-{string.ascii_uppercase}{string.digits}"
    _uuid = ""
    while uuid_int:
        _uuid += chars[uuid_int & 63]
        uuid_int >>= 6
    return f"{_uuid:=>{fixed_length}}" if fixed_length else _uuid
