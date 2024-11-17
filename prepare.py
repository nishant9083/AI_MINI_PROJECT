import subprocess
import warnings

warnings.filterwarnings("ignore")


commands = [
    "git clone https://github.com/AI4Bharat/IndicTrans2.git",
    "cd IndicTrans2/huggingface_interface",
    "python3 -c \"import nltk; nltk.download('punkt')\"",
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

