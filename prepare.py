import subprocess
import warnings

warnings.filterwarnings("ignore")


commands = [    
    "git clone https://github.com/AI4Bharat/IndicTrans2.git",    
    "python3 -c \"import nltk; nltk.download('punkt')\"",
    "cd IndicTrans2/huggingface_interface && git clone https://github.com/VarunGumma/IndicTransToolkit",
    "ls",
    "cd IndicTrans2/huggingface_interface/IndicTransToolkit && python3 -m pip install --editable ./",
    "ls"
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

