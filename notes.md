## Books of interest

1. the annotated turning
1. the elements of computing systems

## Other topics to look into

1. The Halting Problem
1. The Church-Turing Thesis
1. Churches Lambda Calculus

## Number Bases
---

1. BASE 10, Decimal: default in many programming languages if you do not specify
1. BASE 2, Binary: 0b1000 = 8 decimal   
1. BASE 16, Hexidecimal: 0x1000 = 4096 decimal


---
Trick for converting between binary and hex
---

Split number into nybbles (4 bits)

binary:    0101101010101001101110101111011
nybbles:    0101 1010 1010 1001 1011 1010 1111 1011
hex values:  5   A     A    9    B    A    F    B
output hex:  0x5AA9BAFB


## Class Sample Simple Program

```python
import sys

PRINT_BEEJ = 1
HALT = 2

memory = [
  PRINT_BEEJ,
  PRINT_BEEJ,
  HALT,
]

current_index = 0
halted = False

while not halted:
    instruction = memory[current_index]


    if instruction == PRINT_BEEJ:
        print("Beej!")
    elif instruction == HALT:
        halted = True
    else:
        print(f"Unknown instruction at index {current_index})
        sys.exit(1)
        
    current_index += 1
```