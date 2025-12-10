def chatbot():

    import pandas as pd
    data = pd.read_csv('./chatdata.csv')    # reading the chat data
    
    user_input = list(data['user_input'])   # changing the user_input column from chatdatat ot list
    response_msg = list(data['response_msg'])   # changing response message

    i1 = list(enumerate(user_input))    # indexing the user_input
    r1 = list(enumerate(response_msg))  #indexing the response_msg

    while True:
        message = input('user: -> ')    # taking user input
        if message == 'exit':           # to exit if user types 'exit'
            print('bye! take care')
            print('here is your updated list')
            updated_data = {'user_input':user_input,
                            'response_msg':response_msg}    # binding updated data in dictionary
            data = pd.DataFrame(updated_data)               # changed updated into dataframe
            data.to_csv('./chatdata.csv')                   # exported into csv format
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