import sys

PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3
PRINT_REG = 4

memory = [
  PRINT_BEEJ,
  SAVE_REG, # instruction 3: SAVE_REG value 10 in R2
  10,  # value 10
  2, # R2
  PRINT_REG, # PRINT_REG R2
  2,
  HALT,
]
## NOTE: PROGRAM COUNTER SHOULD NOT EVER POINT AT AN OPERAND, ONLY AT INSTRUCTIONS

"""
print("Beej!")
r2 = 10
print(r2)
"""

register = [0] * 8 # Like variables, fixed number of them, fixed names R0, R1, R2 ... R7

pc = 0  # Program Counter, current index, pointer to currently executing instruction
halted = False

while not halted:
    instruction = memory[pc]


    if instruction == PRINT_BEEJ:
        print("Beej!")
        pc += 1

    elif instruction == SAVE_REG:
        value = memory[pc + 1]
        reg_num = memory[pc + 2]
        register[reg_num] = value
        pc += 3
    
    elif instruction == PRINT_REG:
        reg_num = memory[pc + 1]
        print(register[reg_num])
        pc += 2

    elif instruction == HALT:
        halted = True
        pc += 1

    else:
        print(f"Unknown instruction at index {pc}")
        sys.exit(1)
        
    