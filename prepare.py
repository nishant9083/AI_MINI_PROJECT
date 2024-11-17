import subprocess
import warnings

warnings.filterwarnings("ignore")


commands = [
    "git clone https://github.com/AI4Bharat/IndicTrans2.git",
    "cd /content/IndicTrans2/huggingface_interface",
    "python3 -m pip install nltk sacremoses pandas regex mock 'transformers>=4.33.2' mosestokenizer",
    "python3 -c \"import nltk; nltk.download('punkt')\"",
    "python3 -m pip install bitsandbytes scipy accelerate datasets",
    "python3 -m pip install sentencepiece",
    "git clone https://github.com/VarunGumma/IndicTransToolkit",
    "cd IndicTransToolkit",
    "python3 -m pip install --editable ./",
    "cd ..",
]


def execute_commands(commands=commands):
    for command in commands:
        try:
            result = subprocess.run(
                command,
                check=True,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            print(f"Command '{command}' executed successfully.")
            print(f"Output:\n{result.stdout.decode()}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing command '{command}': {e.stderr.decode()}")

