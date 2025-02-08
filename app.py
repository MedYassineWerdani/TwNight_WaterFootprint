from flask import Flask, request, jsonify

from models.water_footprint_model import predict

app = Flask(__name__)

app.route('/', methods=['GET'])
def welcome(): "hi"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json

    # Mapping input data to `predict()` parameters
    result = predict(
        # Personal water use
        showerDuration=data.get('shower_time', 0),
        hasLowFlowShowerhead=data.get('shower_pressure', 'normal') == 'low',
        brushingDuration=data.get('faucet_run_time', 0),
        turnOffWaterWhileBrushing=data.get('faucet_pressure', 'normal') == 'low',
        laundryLoads=data.get('laundry_frequency', 0),
        useEcoWashingMachine=data.get('laundry_manner', 'normal') == 'eco',
        dishwashingMethod=data.get('dishwashing_manner', 'manual'),  
        dishwashingDuration=data.get('faucet_run_time', 0),

        # Diet and consumption habits
        meatConsumption=data.get('meating_frequency', 0),  
        isVegetarian=data.get('diet_type', 'mixed') == 'vegetarian',
        dairyConsumption=data.get('bath_frequency', 0),  # Assuming bath frequency relates to dairy intake?
        usesDairyAlternatives=data.get('diet_type', 'mixed') == 'vegan',
        beverageConsumption=data.get('faucet_run_time', 0),  
        usesReusableCup=data.get('diet_type', 'mixed') == 'eco-conscious',

        # Shopping and recycling habits
        clothingItems=data.get('shop_frequency', 0),
        buysSecondHand=data.get('recycle_clothes', False),
        paperProducts=data.get('have_well', 0),  
        usesRecycledPaper=data.get('have_well', False),  

        # Transportation
        ownsVehicle=data.get('have_car', False),
        vehicleType="gasoline",  # You may need another field for vehicle type
        weeklyDrivingMiles=data.get('miles_driven', 0),

        # Garden & outdoor water use
        gardenSize=data.get('gardenning_frequency', 0),
        usesRainwater=data.get('gardenning_manner', 'normal') == 'rainwater',
        wateringDuration=data.get('gardenning_frequency', 0),
        usesDripIrrigation=data.get('gardenning_manner', 'normal') == 'drip',
        poolSize=data.get('have_well', 0),
        usesPoolCover=data.get('have_well', False)
    )

    return jsonify({"water_footprint": result})

if __name__ == '__main__':
    app.run(debug=True)
