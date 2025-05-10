import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load pre-trained model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Function to get chatbot response
def get_response(user_input):
    # Encode the user input and append EOS token
    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    
    # Generate response from the model
    bot_output = model.generate(new_user_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    
    # Decode the response and return it
    bot_response = tokenizer.decode(bot_output[0], skip_special_tokens=True)
    
    return bot_response

# Main conversation loop
def chat():
    print("Customer Support Chatbot. Type 'exit' to end the conversation.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # If the user types "exit", end the conversation
        if user_input.lower() == "exit":
            print("Goodbye! Have a great day!")
            break
        
        # Get bot response
        bot_response = get_response(user_input)
        
        print(f"Bot: {bot_response}")

# Start the chatbot
if __name__ == "__main__":
    chat()
