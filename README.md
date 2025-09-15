# 4bitcpu
a "4-bit" cpu i made. it uses a 16-bit data bus that is separated into 4-bit chunks. it kinda sucks.
it has a little custom instruction set (if i make more itll be called the kiki isa) that should be very easy to learn.
# OPCODES 
these are more for me to have as a reference. 
ALU opcodes: 
0000 -- NCO (no command)
0001 -- ADD (addition)
0010 -- SUB (subtraction)
0011 -- MUL (multiplication)
0100 -- DIV (division)

REG opcodes:
0000 -- NCO (no command)
0001 -- MOV (move register to other register)
0010 -- CLR (clear register use second Rvalue)
0100 -- MOD (takes output data and puts into Rvalue of your choice)
0101 -- SET (sets a register to specific value {val, reg})

REGADDR opcodes:
0000 -- NCO (no command/register)
0001 -- R0  (register 0)
0010 -- R1  (register 1)
0011 -- R2  (register 2)
0100 -- R3  (register 3)
(NCO is unused in actual programming so disregard it)
# EXAMPLES
example uncompiled DEBUG assembly:
NCO SET 4 R1
NCO SET 2 R2
ADD NCO R1 R2
NCO MOD R3 R3
//this type of code is only meant for debugging/self-compiling.
//instead you should use the compiler to automatically compile it.

example uncompiled assembly 2:
SET 4 R1
SET 2 R2
ADD R1 R2
MOD R3
//you do not need to use the NCO instruction when using the autocompiler.

this program sets register R1 to 4 and register R2 to 2.
it then adds both registers and moves the output (6) to register R3.
# HOW TO USE
you can write a program within the program.asm file (it must be called program.asm) 
then you run in cmd (or unix terminal) build.py program.asm
it will compile and output to the terminal which from there you can copy the hex data and paste it into the logisim rom (its labeled, youll find it)
//output and readability is basially null i have yet to implement any form of usability. 
make sure the pin that says "KEEP AT 1" is at 1.
you can cycle through it by either manually incrementing the clock or automatically setting a tickrate.
"RESET ADDR" button puts rom address at 0 effectively resetting the program.

# OTHER INFO
i may or may not update this.
i threw this together in a couple of hours of free time. i figured id put it here because there arent very many modern logisim cpus anymore.
if you wanna message me my discord tag is draftered. i may or may not respond.
