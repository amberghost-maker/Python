import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama for colored output
colorama.init()

# Welcome message with emojis
print(f"{Fore.CYAN}🌟 Welcome to Sentiment Spy! 🌟{Style.RESET_ALL}")

# Get user name
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent"  # Fallback if no name provided

# Store conversation history as list of tuples: (text, polarity, sentiment_type)
conversation_history = []

# Greeting and instructions
print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a sentence and I will analyze your sentences with TextBlob and show you the sentiment. 🔍")
print(f"{Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

# Main loop
while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    # Handle commands
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE}🛑 Exiting Sentiment Spy. Farewell, Agent {user_name}! 👋{Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🧹 All conversation history cleared!{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}📜 Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                # Choose color and emoji based on sentiment
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😠"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                print(f"{idx}. {color}{emoji} {text} "
                      f"Polarity: {polarity:.2f} {sentiment_type}{Style.RESET_ALL}")

    else:
        # Analyze sentiment with TextBlob
        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity

        # Determine sentiment type
        if polarity > 0:
            sentiment_type = "Positive"
        elif polarity < 0:
            sentiment_type = "Negative"
        else:
            sentiment_type = "Neutral"

        # Save to history
        conversation_history.append((user_input, polarity, sentiment_type))

        # Choose color and emoji for current result
        if sentiment_type == "Positive":
            color = Fore.GREEN
            emoji = "😊"
        elif sentiment_type == "Negative":
            color = Fore.RED
            emoji = "😠"
        else:
            color = Fore.YELLOW
            emoji = "😐"

        # Print current sentiment result
        print(f"{color}{emoji} Polarity: {polarity:.2f} | Sentiment type: {sentiment_type}{Style.RESET_ALL}")