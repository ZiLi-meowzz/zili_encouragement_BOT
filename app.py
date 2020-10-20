print("Title of program: Encouragement bot")
print()
while True:
  description = input("Could you describe how you feel?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("don't worry, be happy :) Everything will get better through time")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep it up! you're AWSOME dude")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("i think it's time to get some rest")
      counter += 1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("why so angry? calm down dude(if you haven't) try to talk to someone...")
      counter += 1
    if each_word == "afraid":
      feelings_list.append("afraid")
      encouragement_list.append("we are all in this together :) find someone to talk about what are you afraid of")
      counter += 1
    if each_word == "depressed":
      feelings_list.append("depressed")
      encouragement_list.append("there is still HOPE, even when your brain tells you there isn't")
      counter += 1
    if each_word == "lonely":
      feelings_list.append("lonely")
      encouragement_list.append("you can try to make friends or just try to occupy your time with doing things that you have not explored")
      counter += 1
    if each_word == "confident":
      feelings_list.append("confident")
      encouragement_list.append("being confident is a good thing and can be a powerful tool but try not to overdo it :) ")
      counter += 1    
    if each_word == "relieved":
      feelings_list.append("relieved")
      encouragement_list.append("")
      counter += 1    
    if each_word == "":
      feelings_list.append("")
      encouragement_list.append("")
      counter += 1    
    if each_word == "":
      feelings_list.append("")
      encouragement_list.append("")
      counter += 1
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different and simpler words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
