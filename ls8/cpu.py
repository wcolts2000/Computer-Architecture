"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""
    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0 # program counter
        self.ir = self.ram[self.pc] # instruction register
        self.fl = 0 # flags -> 00000LGE -> L == <, G == >, E == == 
    def load(self):
        """Load a program into memory."""

        address = 0
        filename = sys.argv[1]
        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        with open(filename) as fp:

            # for instruction in fp:
            for line in fp:
                line = line.split("#")[0]
                line = line.strip()

                if line == "":
                    continue
                self.ram[address] = int(line, 2)
                address += 1

            # print(self.ram)


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")
    
    def ram_read(self, address):
        """
        should accept the address to read and return the value stored
        there
        """
        val = self.ram[address]
        # print("{:010b}".format(val, '08b'))
        return "{:08b}".format(val)

    def ram_write(self, value, address):
        """
        should accept a value to write, and the address to write it to.
        """
        self.reg[address] = value

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X | \n" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        IR = 0
        HLT = 1
        LDI = 2
        PRN = 7
        halted = False
        while not halted:
            IR = self.ram_read(self.pc)
            operand_a = int(str(self.ram_read(self.pc + 1)), 2)
            operand_b = int(str(self.ram_read(self.pc + 2)), 2)
            op_string = int(str(IR)[-4:], 2)
            inc_pc = int(str(IR)[:2], 2) + 1

            # print(IR, "\n", inc_pc, "FFF")
            if op_string == HLT:
                halted = True
                self.pc += inc_pc
            elif op_string == LDI:
                self.ram_write(operand_b, operand_a)
                self.pc += inc_pc
            elif op_string == PRN:
                print(self.reg[operand_a])
                self.pc += inc_pc
            else:
                print(f"ERROR: operation {op_string} unknown")
                sys.exit(1)
