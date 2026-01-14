print("Hello! I am AI Bot. What your name?:")
name = input()
print(f"nIce to meet you, {name}!")
print("How are you feeling today? (good/bad): ")
mood = input().lower()
if mood == "good":
 print("Im glad to hear that")
elif mood == "bad":
    print("Im sorry to hear that. Hope things get better soon")
else:
    print("I see, Sometimes feelings are hard to into words.")
print(f"It was nice chatting to you {name}. Goodbye!")    