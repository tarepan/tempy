print("This is tempy!!")

# Type-checking OK
def please_typecheck1(arg1: int) -> int:
    return 1

# Pyright show warning toward int-string missmatch
def please_typecheck2(arg1: int) -> int:
    return "a"

# Type-checking OK
please_typecheck1(1)

# Pyright show warning toward int-string missmatch
please_typecheck1("a")