from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # URL de la API que quieres consumir
    #api_url = 'https://rickandmortyapi.com/api/character/2'
    api_url = 'https://rickandmortyapi.com/api/character/?name=rick&status=alive'
    
    # Hacer una solicitud GET a la API
    response = requests.get(api_url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir a Json y retornar la respuesta
        data = response.json()
        return jsonify(data)
    else:
        # Manejar el error si la solicitud falló
        return jsonify({'error': 'Failed to retrieve data'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
