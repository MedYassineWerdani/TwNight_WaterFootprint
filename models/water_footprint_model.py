from openai import OpenAI

# Initialize the OpenAI client with OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",  # Replace with your OpenRouter API key
)

def predict(
    showerDuration: float,
    hasLowFlowShowerhead: bool,
    brushingDuration: float,
    turnOffWaterWhileBrushing: bool,
    laundryLoads: int,
    useEcoWashingMachine: bool,
    dishwashingMethod: str, 
    dishwashingDuration: float,

    meatConsumption: float,
    isVegetarian: bool,
    dairyConsumption: float,
    usesDairyAlternatives: bool,
    beverageConsumption: float,
    usesReusableCup: bool,

    clothingItems: int,
    buysSecondHand: bool,
    paperProducts: int,
    usesRecycledPaper: bool,
    ownsVehicle: bool,
    vehicleType: str, 
    weeklyDrivingMiles: float,

    gardenSize: float,
    usesRainwater: bool,
    wateringDuration: float,
    usesDripIrrigation: bool,
    poolSize: float,
    usesPoolCover: bool
):
    # Define the water footprint prompt
    water_footprint_prompt = f"""
    You are an expert in water footprint analysis. Your task is to calculate the total water footprint based on the user's input and provide the results by category.

    Here is some context:
    - Showering: A 10-minute shower uses ~75 liters of water. A low-flow showerhead reduces this by 50%.
    - Brushing teeth: Brushing for 2 minutes with the tap running uses ~6 liters of water. Turning off the tap reduces this to ~0.5 liters.
    - Laundry: One load of laundry uses ~50 liters of water. An eco-friendly washing machine reduces this by 30%.
    - Dishwashing: Manual dishwashing uses ~20 liters per cycle. A dishwasher uses ~10 liters per cycle.
    - Meat consumption: 1 kg of beef requires ~15,000 liters of water, while 1 kg of chicken requires ~4,325 liters.
    - Dairy consumption: 1 liter of milk requires ~1,000 liters of water. Dairy alternatives (e.g., almond milk) require ~400 liters per liter.
    - Beverage consumption: 1 liter of bottled water requires ~3 liters of water to produce. Using a reusable cup reduces this to almost zero.
    - Clothing: Producing one cotton T-shirt requires ~2,700 liters of water. Buying second-hand reduces this to zero.
    - Paper products: 1 kg of paper requires ~10 liters of water. Using recycled paper reduces this by 50%.
    - Transportation: Driving a gasoline car uses ~0.1 liters of water per mile. Electric and hybrid vehicles use significantly less.
    - Gardening: Watering a garden uses ~10 liters per square meter per day. Using drip irrigation reduces this by 50%.
    - Pool: A pool loses ~30 liters of water per day due to evaporation. Using a pool cover reduces this by 70%.

    User Input:
    - Shower: {showerDuration} minutes, low-flow showerhead: {hasLowFlowShowerhead}
    - Brushing: {brushingDuration} minutes, turn off water while brushing: {turnOffWaterWhileBrushing}
    - Laundry: {laundryLoads} loads per week, eco-friendly washing machine: {useEcoWashingMachine}
    - Dishwashing: {dishwashingMethod}, {dishwashingDuration} minutes per day
    - Meat consumption: {meatConsumption} kg of meat per week, vegetarian: {isVegetarian}
    - Dairy consumption: {dairyConsumption} liters per week, uses dairy alternatives: {usesDairyAlternatives}
    - Beverage consumption: {beverageConsumption} liters per week, uses reusable cup: {usesReusableCup}
    - Clothing: {clothingItems} new items per year, buys second-hand: {buysSecondHand}
    - Paper products: {paperProducts} kg per month, uses recycled paper: {usesRecycledPaper}
    - Transportation: Owns a vehicle: {ownsVehicle}, type: {vehicleType}, drives {weeklyDrivingMiles} miles per week
    - Gardening: Garden size: {gardenSize} square meters, uses rainwater: {usesRainwater}, watering duration: {wateringDuration} minutes per day, uses drip irrigation: {usesDripIrrigation}
    - Pool: Pool size: {poolSize} liters, uses pool cover: {usesPoolCover}

    Your Response:
    Calculate the water footprint by category and provide the results in the following format:

    **Shower:** [value] liters/week  
    **Brushing Teeth:** [value] liters/week  
    **Laundry:** [value] liters/week  
    **Dishwashing:** [value] liters/week  
    **Meat Consumption:** [value] liters/week  
    **Dairy Consumption:** [value] liters/week  
    **Beverage Consumption:** [value] liters/week  
    **Clothing:** [value] liters/week  
    **Paper Products:** [value] liters/week  
    **Transportation:** [value] liters/week  
    **Gardening:** [value] liters/week  
    **Pool:** [value] liters/week  
    **Total Water Footprint:** [value] liters/week  

    2. Provide tailored recommendations to reduce the water footprint.
    """

    # Make the API call
    completion = client.chat.completions.create(
        extra_body={},  # No additional body parameters needed
        model="google/gemini-2.0-flash-lite-preview-02-05:free",  # Replace with your desired model
        messages=[
            {
                "role": "user",
                "content": water_footprint_prompt  # Use the water footprint prompt here
            }
        ]
    )

    # Print the response
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content  # Return response if needed
