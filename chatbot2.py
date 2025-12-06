def chatbot():
    # user_input = ['hi', 'how are you', 'fine', 'who are you', 'where do you live', 'how old are you', 'hello', 'how are you', 'what is your name', 'what do you like', 'what do you like', 'who made you', 'okay', 'nothing', 'what', 'hey', 'ok', 'so', 'nice', 'most welcome', 'nope', 'great', 'talk to you later']

    # response_msg = ['hello', 'fine, how are you', 'nice to know this', "I'm a chatbot", 'I live in a computer', "don't know that, just got started", "hi, what's up!", 'fine, doing great', 'my name is bot', 'I like to talk', 'I like to talk', "don't know exactly, may be you!! just kidding", 'okay, anything else', 'okay, so?', "I didn't understood that, be specific", "hey, what's up", 'hey', 'nothing', 'yeah, amazing', 'hmm', 'okay then, talk to you later, or do you wanna say something', 'may be, if you say so', 'okay, see you']

    '''def update():
        with open('./chat_log.csv','a') as fh:
            fh.write(user_input)
            fh.write(response_msg)
            fh.close()
    '''

    import pandas as pd
    # data = {'user_input':['hi', 'how are you', 'fine', 'who are you', 'where do you live', 'how old are you', 'hello', 'how are you', 'what is your name', 'what do you like', 'what do you like', 'who made you', 'okay', 'nothing', 'what', 'hey', 'ok', 'so', 'nice', 'most welcome', 'nope', 'great', 'talk to you later'],
            # 'response_msg':['hello', 'fine, how are you', 'nice to know this', "I'm a chatbot", 'I live in a computer', "don't know that, just got started", "hi, what's up!", 'fine, doing great', 'my name is bot', 'I like to talk', 'I like to talk', "don't know exactly, may be you!! just kidding", 'okay, anything else', 'okay, so?', "I didn't understood that, be specific", "hey, what's up", 'hey', 'nothing', 'yeah, amazing', 'hmm', 'okay then, talk to you later, or do you wanna say something', 'may be, if you say so', 'okay, see you']
            # }
    # data = pd.DataFrame(data)
    data = pd.read_csv('./chatdata.csv')
    # i1 = list(enumerate(user_input))
    # r1 = list(enumerate(response_msg))
    
    user_input = list(data['user_input'])
    response_msg = list(data['response_msg'])

    i1 = list(enumerate(user_input))
    r1 = list(enumerate(response_msg))

    while True:
        message = input('user: -> ')
        if message == 'exit':
            print('bye! take care')
            print('here is your updated list')
            # print(user_input)
            # print(response_msg)
            # data[['user_input','response_msg']] = user_input, response_msg
            updated_data = {'user_input':user_input,
                            'response_msg':response_msg}
            data = pd.DataFrame(updated_data)
            # data['response_msg'] = response_msg
            data.to_csv('./chatdata.csv')

            # update()
            break
        text_num = None
        if message in user_input:
            for num, text in i1:
                if text==message:
                    text_num = num
        else:
            print("sorry, didn't get that")
            user_input.append(message)
            print('please tell me, what should have been my response here.')
            new_response = input()
            response_msg.append(new_response)
            i1 = list(enumerate(user_input))
            r1 = list(enumerate(response_msg))
            print('thanx buddy, now I know. Try asking me again.')
            continue
        for num, text in r1:
            if num == text_num:
                print(f'bot: => {text}')

chatbot()



'''

# the code below is for collecting user_inputs and their responses.
person1 = []
person2 = []

def gen():
    while True:
        text1 = input('question from person1\n')
        text2 = input('reply from person2\n')
        if text1 == 'exit':
            data = {'person1': person1,'person2': person2}
            print(data)
            break
        person1.append(text1)
        person2.append(text2)

gen()
print(person1)
print(person2)

person1 = ['hi', 'how are you', 'fine', 'who are you', 'where do you live', 'how old are you', 'hello', 'how are you', 'what is your name', 'what do you like', 'what do you like', 'who made you', 'okay', 'nothing', 'what']

bot = ['hello', 'fine, how are you', 'nice to know this', "I'm a chatbot", 'I live in a computer', "don't know that, just got started", "hi, what's up!", 'fine, doing great', 'my name is bot', 'I like to talk', 'I like to talk', "don't know exactly, may be you!! just kidding", 'okay, anything else', 'okay, so?', "I didn't understood that, be specific"]

'''