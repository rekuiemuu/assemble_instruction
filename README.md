# UVM Assembler

This project assembles instructions into binary code for use with a UVM (virtual machine).

## Features

The assembler reads an instruction file, converts it into binary format, and generates a log file in JSON format. Supported commands include:

- `90`: Load a constant
- `1`: Read a value from memory
- `62`: Write a value to memory
- `137`: Unary operation `sqrt()`

## Installation

Make sure you have Python 3.7+ installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/uvm-assembler.git
   cd uvm-assembler
   ```

2. Install dependencies (if needed in the future):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The script accepts three required arguments:

- `--input`: Path to the input assembly file.
- `--output`: Path to the output binary file.
- `--log`: Path to the log file.

### Example Command

```bash
python assembler.py --input input.asm --output output.bin --log log.json
```

### Input File Format

Each line in the input file should represent an instruction, e.g.:

```asm
90 42 0
1 100 200 1
62 300 400
137 500 0 1
```

- Lines starting with `#` are treated as comments and ignored.
- Empty lines are also ignored.

### Output Log Format

The log is generated in JSON format and contains the converted instructions:

```json
[
    {
        "instruction": "90 42 0",
        "binary": "5a000000002a000000000000000000"
    },
    {
        "instruction": "1 100 200 1",
        "binary": "01000000006400000000000000c80000000000000001"
    }
]
```

## Testing

You can test the program using an example `input.asm` file.

1. Create a file `input.asm` with the following content:
   ```asm
   # Example input file
   90 42 0
   1 100 200 1
   ```

2. Run the program:
   ```bash
   python assembler.py --input input.asm --output output.bin --log log.json
   ```

## Supported Commands

| Command | Description                  | Format                  |
|---------|------------------------------|-------------------------|
| `90`    | Load a constant              | `<B Q Q>`              |
| `1`     | Read from memory             | `<B Q Q B>`            |
| `62`    | Write to memory              | `<B Q Q>`              |
| `137`   | Unary operation `sqrt()`     | `<B Q B Q>`            |

