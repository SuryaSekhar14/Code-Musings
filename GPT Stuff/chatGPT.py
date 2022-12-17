# import sys
# from chatgpt import Conversation

# conversation = Conversation()

# # Stream the message as it arrives.
# for chunk in conversation.stream("We are going to start a conversation. I will speak English and you will speak Portuguese."):
#     print(chunk, end="")
#     sys.stdout.flush()

# # Wait until the message is fully received.
# print(conversation.chat("What's the color of the sky?"))

# # The AI will forget it was speaking Portuguese
# conversation.reset()
# print(conversation.chat("What's the color of the sun?"))

import sys
from chatgpt import Conversation
from chatgpt import ChatgptError, ChatgptErrorCodes

conversation = Conversation()

try:

    for chunk in conversation.stream("Hello, world!"):
        print(chunk, end="")
        sys.stdout.flush()

except ChatgptError as chatgpt_error:

    message = chatgpt_error.message
    code = chatgpt_error.code

    if code == ChatgptErrorCodes.INVALID_ACCESS_TOKEN:
        print("Invalid token")