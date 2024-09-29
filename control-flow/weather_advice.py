Weather = input("What's the weather like today?(sunny/rainy/cold): ")
if Weather == "sunny" or Weather == "Sunny":
    print("Wear a t-shirt and sunglasses.")
elif Weather == "rainy" or Weather == "Rainy":
    print("Don't forget your umbrella and a raincoat.")
elif Weather == "cold" or Weather == "Cold":
    print("Make sure to wear coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
