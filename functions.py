import pandas as pd
path = "/home/nitish/Nitish/Personal/I-lost-you/chat.txt"

def read_file(file):
    '''Reads Whatsapp text file into a list of strings'''
    x = open(file,'r', encoding = 'utf-8') #Opens the text file into variable x but the variable cannot be explored yet
    y = x.read() #By now it becomes a huge chunk of string that we need to separate line by line
    content = y.splitlines() #The splitline method converts the chunk of string into a list of strings
    return content

def prepare_data(content):
    df = pd.DataFrame(content)
    df.columns = ["text"]
    df["text"] = df["text"].apply(lambda x: x.strip())
    # df["len"] = df["text"].apply(lambda x: len(x))
    df[["datetime", "Name_Msg"]] = df.text.str.split(" - ", expand=True)
    df["Name_Msg"] = df.groupby(['Group'])['Data'].shift(1)
    print(df.columns)
    print(df)

def train_chat_model(chat_file):
    content = read_file(chat_file)
    prepare_data(content[:4])


train_chat_model(path)