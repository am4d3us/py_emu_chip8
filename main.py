import numpy as np


class Stack:
    def __init__(self, size):
        self.stack = np.zeros(size, dtype=np.uint8)
        self.top = size - 1
        self.pointer = 0

    def push(self, value: np.uint8) -> np.uint8 | None:
        if self.full():
            return None

        self.stack[self.pointer] = value
        self.pointer += 1

        return self.pointer

    def pop(self) -> np.uint8 | None:
        if self.empty():
            return None

        value = self.stack[self.pointer]
        self.pointer -= 1
        return value

    def full(self) -> bool:
        return self.pointer == self.top

    def empty(self) -> bool:
        return self.pointer == 0


class Emulator:
    def __init__(self):
        self.memory = np.zeros(4096, dtype=np.uint8)
        self.gpio = np.zeros(16, dtype=np.uint8)

        self.index = 0  # The 'I' register.
        self.pc = 0
        self.opcode = 0

        self.stack = np.zeros(16, dtype=np.uint8)
        self.sp = 0

        self.timer_delay = 0
        self.timer_sound = 0

        self.keyboard = np.zeros(16, dtype=np.uint8)
        self.display = np.zeros((64, 32), dtype=np.uint8)

    def _get_x(self):
        return (self.opcode >> 8) & 0xF

    def _get_y(self):
        return (self.opcode >> 4) & 0xF

    def _get_kk(self):
        return self.opcode & 0xFF

    def _00E0(self):
        self.display = np.zeros_like(self.display)

    def _00EE(self):
        self.pc = self.stack.pop()

    def _1nnn(self):
        self.pc = self.opcode & 0x0FFF

    def _2nnn(self):
        self.stack.push(self.pc)
        self._1nnn(self.opcode)

    def _3xkk(self):
        if self.gpio[self._get_x()] == self._get_kk():
            self.pc += 2

    def _4xkk(self):
        if self.gpio[self._get_x()] != self._get_kk():
            self.pc += 2

    def _5xy0(self):
        if self.gpio[self._get_x()] == self.gpio[self._get_y()]:
            self.pc += 2

    def _6xkk(self):
        self.gpio[self._get_x()] = self._get_kk()

    def _7xkk(self):
        self.gpio[self._get_x()] += self._get_kk()


def main():
    emulator = Emulator()

    print("Hello from py-emu-chip8!")


if __name__ == "__main__":
    main()
