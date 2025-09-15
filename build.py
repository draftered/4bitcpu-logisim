# build.py
import sys
from assembler import assemble

if len(sys.argv) < 2:
    print("Usage: build.py program.asm")
    sys.exit(1)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    program = f.read()

assembled = assemble(program)

print("Output Hex:")
for word in assembled:
    print(word)
