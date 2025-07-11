import re
import pandas as pd

def preprocess(data):
    # Match date pattern
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    
    # Split chat into messages and timestamps
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    # Create DataFrame
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    
    # Convert dates
    try:
        df['message_date'] = pd.to_datetime(df['message_date'], format='%m/%d/%y, %H:%M - ')
    except:
        df['message_date'] = pd.to_datetime(df['message_date'], errors='coerce')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Extract user and message
    users = []
    messages_list = []

    for message in df['user_message']:
        entry = re.split(r'([^:]+):\s', message, maxsplit=1)
        if len(entry) == 3:
            users.append(entry[1])
            messages_list.append(entry[2])
        else:
            users.append('group_notification')
            messages_list.append(entry[0])

    # Check lengths before assigning
    if len(df) != len(users):
        raise ValueError(f"Mismatch in lengths: df={len(df)}, users={len(users)}")

    df['user'] = users
    df['message'] = messages_list
    df.drop(columns=['user_message'], inplace=True)

    # Add additional time columns
    df['date_only']=df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num']=df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.date
    df['day_name']=df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    
    period=[]
    for hour in df[['day_name','hour']]['hour']:
        if hour==23:
            period.append(str(hour)+ "-"+ str('00'))
        elif hour==0:
            period.append(str('00')+ "-"+ str(hour+1))
        else:
            period.append(str(hour)+ "-"+ str(hour+1))
    df['period']=period
    
    return df

