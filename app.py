from flask import Flask, render_template, request, jsonify
from config import Config
from services.recipe_service import RecipeService

app = Flask(__name__)
app.config.from_object(Config)

recipe_service = RecipeService(app.config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_recipes():
    try:
        data = request.get_json()
        ingredients = data.get('ingredients', [])
        dietary_restrictions = data.get('dietary_restrictions', [])
        cuisine = data.get('cuisine', '')
        
        recipes = recipe_service.get_recommendations(
            ingredients, dietary_restrictions, cuisine
        )
        
        return jsonify({'success': True, 'recipes': recipes})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)