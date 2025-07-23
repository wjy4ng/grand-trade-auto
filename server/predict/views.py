from django.http import JsonResponse
import pandas as pd
import json
import sys
import os
from .main import App

# --- Model Loading ---
# This part will be executed once when the Django server starts.
# It initializes the App, which loads data and trains the model.
print("Initializing App and training model...")
app = App()
app.run()  # This calls model.train() and model.evaluate()
print("Model ready.")


def predict_price(request):
    if request.method == 'POST':
        try:
            # Assuming the request body is JSON
            data = json.loads(request.body)

            # Create a DataFrame from the input data
            input_df = pd.DataFrame([{
                '제조사': data.get('manufacturer'),
                '모델명': data.get('model'),
                '주행거리': int(data.get('mileage')),
                '연식': int(data.get('year'))
            }])

            # Make a prediction using the model from the app instance
            prediction = app.model.predict(input_df)

            # Return the prediction as JSON
            # Use .tolist() to make it JSON serializable
            return JsonResponse({'predicted_price': prediction.tolist()})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Only POST requests are accepted'}, status=405)