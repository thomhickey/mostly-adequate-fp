# impure
minimum = 21;
checkAge = lambda age: age >= minimum

print(checkAge(10))  # false


# pure
def checkAgePure(age: int) -> bool:
    minimum = 21
    return age >= minimum

print(checkAgePure(10)) # false