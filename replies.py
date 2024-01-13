from random import choice, randint

def get_reply(user_input):
    lowered = user_input.lower()

    if lowered == '':
        return 'Well you\'re awfully quiet today!'
    elif 'hello' in lowered:
        return 'Hello there'
    elif 'how are you' in lowered:
        return 'Good Thanks!'
    elif 'bye' in lowered:
        return 'See you'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,6)}'
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Can you rephrase that?'])