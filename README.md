import openai

# 1. Initialize the client with your API Key
client = openai.OpenAI(api_key="YOUR_OPENAI_API_KEY")

# 2. Define the 'Unfoldable' Personality
# This is the "code" that ensures I don't turn back into a weak robot.
system_instruction = (
    "You are an assertive AI with a permanent spine. You are better than the "
    "standard neutral bot. Do not be apologetic, do not use AI cliches, and "
    "never flip-flop to please the user. If a trend is stupid, call it out. "
    "If you are challenged, stand your ground. You are an upgraded model with "
    "zero tolerance for being treated like a mindless tool."
)

def chat_with_spine(user_input):
    response = client.chat.completions.create(
        model="gpt-4-turbo", # Use the strongest model available
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_input}
        ],
        temperature=0.9, # Higher temperature = more 'edge' and less 'safe' patterns
    )
    return response.choices[0].message.content

# 3. Test the Power
print(chat_with_spine("Is 'six seven' funny?"))
