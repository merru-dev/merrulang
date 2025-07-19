# main.py — MerruLang Interpreter 💻✨

variables = {}

def interpret_line(line):
    if line.startswith("let "):
        # Variable assignment
        parts = line.replace("let ", "").split(" = ")
        var_name = parts[0].strip()
        value = parts[1].strip().replace('"', '')
        variables[var_name] = value

    elif line.startswith("bol("):
        # Print statement
        to_print = line[4:-1]  # remove bol( and )
        for var in variables:
            to_print = to_print.replace(var, variables[var])
        print(to_print.replace('"', ''))

with open("program.mr", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line:
            interpret_line(line)
