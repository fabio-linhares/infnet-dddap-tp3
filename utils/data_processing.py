import json

def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Adicione mais funções utilitárias conforme necessário