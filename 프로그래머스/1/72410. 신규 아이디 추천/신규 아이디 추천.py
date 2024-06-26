import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    new_id = re.sub('\.+', '.', new_id)
    new_id = re.sub('^\.|\.$', '', new_id)
    
    if new_id == '':
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub('\.$', '', new_id)
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    
    return new_id