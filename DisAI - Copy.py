import discord
from discord.ext import commands

import openai 


openai.api_key =  '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' 


# Create an instance of the bot with intents
intents = discord.Intents.all()
intents.typing = False  # Disable typing events for simplicity, can be enabled if needed
bot = commands.Bot(command_prefix='!', intents=intents)

# Event triggered when the bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user.name}')

# Event triggered when a message is received
@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself to prevent loops
    if message.author == bot.user:
        return

    if "!" not in message.content:
         return

  
    response = generate_response(message.content)

    await message.channel.send(response)

    # Process the message here and generate a response
 
# Function to generate a response based on the input message
#def generate_response(message):
    # Your AI chat bot logic goes here
    # You can use NLP libraries, machine learning models, or any other technique

    # Return a response
  #  return "This is a sample response."

def generate_response(message):
    # Send user message to ChatGPT API
    response = openai.Completion.create(
        engine='text-davinci-002',  # Specify the ChatGPT engine
        prompt=message,
        temperature=0.6,  # Controls the randomness of the AI's response
        max_tokens=50,  # Limit the length of the generated response
        n=1,  # Specify the number of responses to generate
        stop=None  # Specify a stopping condition for the response generation
    )
    
    # Extract the generated response from the API response
    ai_response = response.choices[0].text.strip()
    
    # Return the AI-generated response
    return ai_response

# Run the bot using the bot token
bot.run('MTExMDE4Mzc0MzMyMDI0MDEzOA.GVbMMl.FVDQeWyftC8gDZdhFswwkshb8k0wJqMxDp0tjQ')
