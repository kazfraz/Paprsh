import os
import subprocess
import configparser

def parse_config_file(config_file_path='test.paprcf'):
    full_path = os.path.expanduser(config_file_path)
    if not os.path.exists(full_path):
        print(f"Configuration file '{full_path}' not found.")
        return None

    config = configparser.ConfigParser()
    config.read(full_path)
    return config

def main():
    config = parse_config_file('test.paprcf')
    prompt = config['Shell'].get('prompt', 'paprsh> ')

    while True:
        user_input = input(prompt)
        if user_input.lower() == 'exit':
            break
        try:
            # Execute the command
            output = subprocess.run(user_input.split(), capture_output=True, text=True, check=True)
            print(output.stdout)
        except FileNotFoundError:
            print("Command not found:", user_input.split()[0])
        except subprocess.CalledProcessError:
            pass  # Ignore other subprocess errors

if __name__ == "__main__":
    main()

