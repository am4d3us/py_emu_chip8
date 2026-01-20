import numpy as np


class Emulator:
        """
        An emulator for the CHIP-8 interpreted programming language.

        Memory Specification:
        ---
        Commonly implemented on 4K systems with 4096 8-bit memory locations,
        i.e. RAM (Random-Access Memory), sectioned according to the diagram below:

        +---------------+= 0xFFF (4095) End of Chip-8 RAM
        |               |
        |               |
        |               |
        |               |
        |               |
        | 0x200 to 0xFFF|
        |     Chip-8    |
        | Program / Data|
        |     Space     |
        |               |
        |               |
        |               |
        +- - - - - - - -+= 0x600 (1536) Start of ETI 660 Chip-8 programs
        |               |
        |               |
        |               |
        +---------------+= 0x200 (512) Start of most Chip-8 programs
        | 0x000 to 0x1FF|
        | Reserved for  |
        |  interpreter  |
        +---------------+= 0x000 (0) Start of Chip-8 RAM


        Register Specification:
        ---
        16 8-bit GPIO (General Purpose Input/Output) registers, referred to as
        'Vx', where 'x' is a hexadecimal digit. The 'VF' is a special register,
        however, as it doubles as a flag and shall be avoided.

        One 16-bit register, referred to as 'I', where only the 12 lowest bits
        are utilized, used to store memory addresses.


        Timer Specification:
        ---
        Two timers, both of which actively count down at 60 hertz whenever the
        respective associated register is non-zero until they reach zero:
        - Delay: intended to be used for timing game-events. (READ/WRITE)
        - Sound: intended to be used for sound effects. (WRITE)


        Input Specification:
        ---
        Hex keyboard with 16 keys ranging from 0 to F.
        ...


        Graphics Specification:
        ---
        ...
        """

    def __init__(self):
        self.memory = np.zeros(4096, dtype=np.uint8)
        self.gpio = np.zeros(16, dtype=np.uint8)
        self.index = 0 # The 'I' register.

        self.timer_delay = 0
        self.timer_sound = 0

        self.keyboard = np.zeros(16, dtype=np.uint8)
        self.display = np.zeros((32, 64), dtype=np.uint8)





def main():
    emulator = Emulator()

    print("Hello from py-emu-chip8!")


if __name__ == "__main__":
    main()
