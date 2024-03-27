from django.shortcuts import render
from .forms import RecommendationForm
from .my_processing_script import process_input

def my_view(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            # Process the form data
            input_data = {
                'npk1': form.cleaned_data['npk1'],
                'npk2': form.cleaned_data['npk2'],
                'npk3': form.cleaned_data['npk3'],
                'rainfall': form.cleaned_data['rainfall'],
                'temperature': form.cleaned_data['temperature'],
                'humidity': form.cleaned_data['humidity'],
                'soil_ph': form.cleaned_data['soil_ph'],
            }
            processed_result = process_input(input_data)
            return render(request, 'result.html', {'result': processed_result})
    else:
        form = RecommendationForm()
    return render(request, 'recommend.html', {'form': form})

def submit_recommendation_view(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            input_data = form.cleaned_data
            processed_result = process_input(input_data)
            # Do something with the processed result
            return redirect('result.html')  # Redirect to a success page
    else:
        form = RecommendationForm()
    return render(request, 'recommend.html', {'form': form})