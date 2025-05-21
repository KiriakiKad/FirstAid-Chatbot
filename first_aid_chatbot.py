import re
import random 

#chatbot responses patterns and corresponding replies
patterns = [
   (r'\b(hello|hey|hi)\b', ["Hello, How can I help you with first aid today?", "Hi! Are you in need of any first aid assistance?"]),
   (r'.*\b(pass(ing|ed)? out|los(ing|t)? consciousness|faint(ing|ed)?\b).*', ["You mentioned {0}. if there is no breathing, CPR should be started immediately. Otherwise they should be placed in the recovery position."]),
   (r'.*(how do i|how can i|what is the way to).*CPR.*', [
    "To perform CPR, follow these steps:\n"
    "1. Check if the person is responsive and breathing normally.\n"
    "2. If not, call emergency services immediately (e.g., 112).\n"
    "3. Begin chest compressions: push hard and fast in the center of the chest — 30 compressions at a rate of 100–120 per minute.\n"
    "4. If trained, give 2 rescue breaths after every 30 compressions.\n"
    "5. Continue CPR until emergency help arrives or the person starts breathing normally."]),
    (r'\D*\b(30|how many|number of)\b\D*(compressions|CPR)\D*', ["30 is the correct number of compressions per CPR cycle."]),
    (r'\D*\b(([0-2]?[0-9]|[3-9][1-9]))\b\D*(compressions|CPR)\D*', ["{0} compressions is not the recommended amount. CPR cycles usually involve 30 compressions."]),
    (r'.*\b(nose|nosebleed)\b.*', ["For a nosebleed, lean forward and pinch the nose for 10 minutes. Don't tilt your head back."]),
    (r'.*\b(leg|arm|head|torso|back|chest|body)\b.*(bleeding)?.*', ["For bleeding from the {0}, apply direct pressure to the wound using a clean cloth or bandage. Elevate the injured part if it's possible."]),
    (r'.*\b(bleeding)\b.*', ["Where is the bleeding happening? Is it from the nose or another part of the body? Please specify."]),
    (r'.*\b(chok(ing|e)?|gasping)\b.*', ["If someone is choking, encourage them to cough or perform back blows. But if the person is unconscious from choking{1}, begin CPR immediately and call for help.",
     "For choking, perform 5 back blows followed by 5 abdominal thrusts if coughing doesn’t work. If the person loses consciousness, call 112 and start CPR."]),
    (r'.*\b(seizure|epilepsy)\b.*', ["If someone is having a seizure, do not try to hold them down. Move them to a safe place away from dangerous objects. Also, protect their head with a soft object if possible and do not try to put anything in their mouth. If the seizure lasts for more than 5 minutes or they have multiple seizures in a row, call emergency services immediately.",
    "During a seizure, stay with the person, time the seizure, and clear the area of sharp objects. Call for help if it lasts too long.",
    "Seizures can be scary, but remain calm. Cushion the person’s head, loosen tight clothing, and never put anything in their mouth."]),
    (r'.*\b(call.*emergency|emergency number|what number.*call|how to call.*help)\b.*', ["In any serious or life-threatening situation, make sure to call emergency services immediately by dialing 112.",
    "Dial 112 for immediate emergency assistance anywhere in the EU.",
    "You should call 112 in case of an emergency to get help from police, fire, or ambulance services."]),
    (r'.thank you|thanks', ["You're welcome! I'm here if you need anything else.","Glad I could help. Let me know if you need more assistance."])

]

# Function to process user input and respond based on patterns
def respond(user_input):
    for pattern, responses in patterns:
        match = re.search(pattern, user_input.strip(), re.IGNORECASE)
        if match:
            return random.choice(responses).format(*match.groups())
    return "I'm not sure how to help with that. Could you describe the situation differently?"

# Main function to run the chatbot loop
def chatbot():
    print("Welcome to the First Aid Assistant chatbot. Type 'exit', 'quit' or 'bye' anytime to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("First Aid Assistant: Stay safe! Goodbye.")
            break
        response = respond(user_input)
        print("First Aid Assistant:", response)

if __name__ == "__main__":
    chatbot()
