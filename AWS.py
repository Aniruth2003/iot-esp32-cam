import boto3
import csv 

with open('credentials.csv', 'r') as file:
    next(file)
    reader = csv.reader(file)

    for line in reader:
        access_key_id = line[2]
        secret_access_key_id = line[3]

client = boto3.client('rekognition',
    region_name='us-east-1',
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key_id)

def isBird(photo):
    with open(photo, 'rb') as f:
        source_bytes = f.read()

    response = client.detect_labels(Image={'Bytes':source_bytes})

    # print(response)

    flag = False
    # print('Detected labels in ' + photo,"\n")
    # print("AWS modified response labels :")
    for label in response['Labels']:
        if 'Bird' in label['Name'] :
            flag = True

        # print(label['Name'] + ' : ' + str(label['Confidence']))

    return flag

def isHuman(photo):
    with open(photo, 'rb') as f:
        source_bytes = f.read()

    response = client.detect_labels(Image={'Bytes':source_bytes})

    # print(response)

    flag = False
    # print('Detected labels in ' + photo,"\n")
    # print("AWS modified response labels :")
    for label in response['Labels']:
        if 'Human' in label['Name'] :
            flag = True
        elif 'Person' in label['Name'] :
            flag = True
        
        # print(label['Name'] + ' : ' + str(label['Confidence']))

    return flag
if __name__ == '__main__' : 
    print(isBird('img.png'))