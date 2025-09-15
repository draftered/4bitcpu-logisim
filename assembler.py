# assembler.py

ALU_OPCODES = {
    "NCO": "0000",
    "ADD": "0001",
    "SUB": "0010",
    "MUL": "0011",
    "DIV": "0100",
}

REG_OPCODES = {
    "NCO": "0000",
    "MOV": "0001",
    "CLR": "0010",
    "MOD": "0100",
    "SET": "0101",
}

REGADDR_OPCODES = {
    "NCO": "0000",
    "R0":  "0001",
    "R1":  "0010",
    "R2":  "0011",
    "R3":  "0100",
}


def assemble_line(line, lineno):
    line = line.strip()
    if not line or line.startswith(";"):
        return None  # ignore blank or comment lines

    parts = line.split()
    op = parts[0].upper()

    alu = "0000"
    reg = "0000"
    r1 = "0000"
    r2 = "0000"

    if op in ALU_OPCODES:
        alu = ALU_OPCODES[op]
        if len(parts) >= 3:
            r1 = REGADDR_OPCODES.get(parts[1].upper(), "0000")
            r2 = REGADDR_OPCODES.get(parts[2].upper(), "0000")

    elif op in REG_OPCODES:
        reg = REG_OPCODES[op]

        if op == "MOV" and len(parts) == 3:
            r1 = REGADDR_OPCODES.get(parts[1].upper(), "0000")
            r2 = REGADDR_OPCODES.get(parts[2].upper(), "0000")

        elif op == "CLR" and len(parts) == 2:
            r2 = REGADDR_OPCODES.get(parts[1].upper(), "0000")

        elif op == "MOD" and len(parts) == 2:
            r2 = REGADDR_OPCODES.get(parts[1].upper(), "0000")

        elif op == "SET" and len(parts) == 3:
            # format: SET value reg
            val = int(parts[1]) & 0xF
            r1 = f"{val:04b}"
            r2 = REGADDR_OPCODES.get(parts[2].upper(), "0000")

    else:
        raise SyntaxError(f"Line {lineno}: Unknown instruction '{op}'")

    word = alu + reg + r1 + r2
    return f"{int(word, 2):04X}"


def assemble(program_text):
    output = []
    for i, line in enumerate(program_text.splitlines(), 1):
        code = assemble_line(line, i)
        if code:
            output.append(code)
    return output

