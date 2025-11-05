
import requests

# URL de exemplo
url = "https://api.github.com"

# Faz uma requisição GET
response = requests.get(url)

# Verifica se deu certo
if response.status_code == 200:
    print("✅ Requisição bem-sucedida!")
    print("Conteúdo da resposta:")
    print(response.json())  # Mostra o JSON retornado
else:
    print("❌ Erro na requisição:", response.status_code)

