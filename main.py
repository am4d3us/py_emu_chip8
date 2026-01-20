import numpy as np


class Emulator:
        """
        An emulator for the CHIP-8 interpreted programming language.

        Memory Specification:
        The CHIP-8 language is capable of accessing 4096 bytes of RAM,
        sectioned according to the following diagram:

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
        """

    def __init__(self):
        self.keyboard = np.zeros(16, dtype=np.uint8)
        self.display = np.zeros((32, 64), dtype=np.uint8)

        self.memory = np.zeros(4096, dtype=np.uint8)
        self.gpio = np.zeros(16, dtype=np.uint8)

        self.index = 0
        self.pc = 0

        self.timer_delay = 0
        self.timer_sound = 0


def main():
    emulator = Emulator()

    print("Hello from py-emu-chip8!")


if __name__ == "__main__":
    main()
