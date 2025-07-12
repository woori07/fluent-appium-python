import re

def strip_stacktrace(exc: Exception) -> str:
    """
    에러 메시지에서 스택 트레이스를 제거하는 함수
    """
    if isinstance(exc, Exception):
        msg = str(exc)
    else:
        msg = str(exc)

    lines = msg.splitlines()
    filtered = [line for line in lines if not line.strip().startswith(('File', 'Traceback'))]

    filtered = [line for line in filtered if line.strip()]
    return '\n'.join(filtered) if filtered else msg
