import struct
import json

class UVM:
    def __init__(self):
        self.memory = [0] * 1024  # Инициализация памяти
    
    def execute(self, binary_path, result_path, memory_range):
        with open(binary_path, 'rb') as binary_file:
            data = binary_file.read()

        i = 0
        while i + 18 <= len(data):  # Проверяем на наличие 17 байтов
            command = data[i]
            if command == 90:  # Загрузка константы
                _, b, c = struct.unpack('<B Q Q', data[i:i+17])
                self.memory[b] = c
                i += 17
            elif command == 1:  # Чтение из памяти
                _, b, c, d = struct.unpack('<B Q Q B', data[i:i+18])
                source_value = self.memory[c]
                target_address = source_value + d
                self.memory[b] = self.memory[target_address]
                i += 18
            elif command == 62:  # Запись в память
                _, b, c = struct.unpack('<B Q Q', data[i:i+17])
                self.memory[b] = self.memory[c]
                i += 17
            elif command == 137:  # sqrt()
                _, b, c, d = struct.unpack('<B Q B Q', data[i:i+18])
                source_value = self.memory[d]
                target_address = b + c
                self.memory[target_address] = int(source_value**0.5)
                i += 18
            else:
                raise ValueError(f"Unknown command: {command}")
        
        # Сохранение диапазона памяти в файл
        result = {f"memory[{addr}]": value for addr, value in enumerate(self.memory[memory_range[0]:memory_range[1]])}
        with open(result_path, 'w') as result_file:
            json.dump(result, result_file, indent=4)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--binary", required=True, help="Path to the binary file")
    parser.add_argument("--result", required=True, help="Path to the result file")
    parser.add_argument("--range", required=True, help="Memory range (start:end)")

    args = parser.parse_args()
    memory_range = list(map(int, args.range.split(":")))

    uvm = UVM()  # Создание объекта класса
    uvm.execute(args.binary, args.result, memory_range)




