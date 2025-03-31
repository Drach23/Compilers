def validate_if_else(s):
    return "if" in s and "else" in s
input_str = "else: print('No')"
if validate_if_else(input_str):
    print("Sentencia valida.")
else:
    print("Sentencia invalida.")