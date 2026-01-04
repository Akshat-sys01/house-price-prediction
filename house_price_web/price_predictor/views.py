import logging
from django.shortcuts import render
from price_predictor.forms import HousePriceForm
from price_predictor.ml.predictor import predict_price_with_confidence

logger = logging.getLogger('price_predictor')

# Create your views here.
def home(request):
    result = None
    form = HousePriceForm()

    if request.method == 'POST':
        form = HousePriceForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            logger.info(
                "Prediction request received | area=%s, bedrooms=%s, bathrooms=%s, age=%s",
                data['area'], data['bedrooms'], data['bathrooms'], data['age']
            )

            try:
                result = predict_price_with_confidence(
                    area=data['area'],
                    bedrooms=data['bedrooms'],
                    bathrooms=data['bathrooms'],
                    age=data['age']
                )
                logger.info("Prediction successful | price=%s", result['prediction'])

            except Exception as e:
                logger.error("Prediction failed | error=%s", str(e))
        else:
            logger.warning("Form validation failed")

    return render(request, 'home.html', {
        'form': form,
        'result': result,
    })