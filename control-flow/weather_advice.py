weather = input("What's the weather like today?(sunny/rainy/cold): ")
if weather == "sunny" or weather == "Sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy" or weather == "Rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold" or weather == "Cold":
    print("Make sure to wear coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
