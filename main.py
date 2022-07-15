def upper(string:str) -> str:
    return string.upper()

def lower(string:str) -> str:
    return string.lower()

def test(func:complex) -> str:
    Result = func("This is first class python")
    print(Result)

test(upper)
test(lower)