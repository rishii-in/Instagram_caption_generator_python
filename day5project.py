print("--------------------📸 Instagram caption Generator 📸----------------------------")
print()
print("Tell me about your mood right now !! ")
print("-----------------------------------------")
print("1.Happy 😊")
print("2.Sad 😔")
print("3.Weather 💭")
print("4.Tradition 🙏")
print("5.Bike or Car Ride 🚗")
print("6.Food 🍜")
print("-------------------------------------------")
print()
choice=int(input("enter your choice(1-6) ✅ :"))
print()
if choice==1:
    print("😊 Happiness isn’t a mood, it’s my vibe right now ✨")
    print(f"🎵 song - yahoon yahoon from Mirchi")

elif choice==2:
    print("😔 I wish I could go back to when everything felt right.")
    print(f"🎵 song - Chitti Adugu from Most eligible bachelor")
elif choice==3:
    type=input("enter your current weather type (sunny/rainy): ").lower()
    if type=="rainy":
        print("💭 Rain turns ordinary moments into something magical.")
        print(f"🎵 Song - Arere Vaana from Awaara")
    elif type=="sunny":
        print("☀️ Sunlight touched everything—and somehow, me too")
        print(f"🎵 Song - Seethakalam from Son of satyamurthi")
    else:
        print("Invalid Weather type ❌")
elif choice==4:
    place=input("Enter place (temple/home) : ").lower()
    if place=="temple":
        print("🙏 Blessed and dressed in tradition ✨")
        print("🎵 Song - Maduramee from Arjun Reddy")
    elif place=="home":
        print("🌸 Tradition never needs a special place… home is enough")
        print("🎵 Song - Inkem Inkem song from Geetha Govindam")
    else:
        print("Invalid place ❌ ")
elif choice==5:
    print("🚗 Just me, my playlist, and the road 🎶 ")
    print("🎵 Song - Blinding Lights by Weekend ")
elif choice==6:
    print("❤️ Some love stories are written with words… mine is written with food 🍜")
    print("🎵 Song - Sahiba song from Hindi")
else:
    print("Invalid choice ❌ ")