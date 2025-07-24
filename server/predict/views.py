from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import pandas as pd
import json
from .main import App

print("Initializing App and training model...")
app = App()
app.run()
print("Model ready.")


@csrf_exempt
def predict_price(request):
    if request.method == 'POST':
        try:
            print(f"Request body: {request.body}") # Add this line
            data = json.loads(request.body)
            input_df = pd.DataFrame([{
                '제조사': data.get('manufacturer'),
                '모델명': data.get('model'),
                '주행거리': int(data.get('mileage')),
                '연식': int(data.get('year'))
            }])
            prediction = app.model.predict(input_df)
            print(prediction)
            return JsonResponse({'predicted_price': prediction.tolist()})
        except Exception as e:
            print(f"Error during prediction: {e}") # Add this line to print the error
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Only POST requests are accepted'}, status=405)