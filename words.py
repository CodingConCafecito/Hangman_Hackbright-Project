# import random

word_list = ['acorn', 'admit', 'adopt', 'adult', 'agree', 'album', 'allow', 'anger', 'apple', 'apply', 'argue', 'arise', 'armor', 'avoid', 'award', 'awful', 'bagel', 'baker', 'beach', 'beard', 'begin', 'berry', 'birth', 'blame', 'blank', 'block', 'blood', 'blues', 'blush', 'bonus', 'boxer', 'brain', 'bread', 'break', 'bring', 'brown', 'brush', 'build', 'burst', 'candy', 'carry', 'catch', 'cause', 'chain', 'chair', 'chalk', 'chaos', 'cheap', 'check', 'chewy', 'chief', 'chili', 'cigar', 'claim', 'class', 'clean', 'clear', 'click', 'climb', 'clock', 'cloud', 'coach', 'coast', 'color', 'comic', 'coral', 'corny', 'count', 'court', 'cream', 'crime', 'crowd', 'curls', 'cycle', 'dairy', 'daisy', 'dance', 'death', 'doubt', 'drama', 'dream', 'dress', 'drink', 'drive', 'eagle', 'earth', 'easer', 'elbow', 'enemy', 'enjoy', 'enter', 'error', 'event', 'exist', 'fault', 'field', 'fight', 'final', 'flame', 'floor', 'focus', 'force', 'frame', 'fried', 'front', 'fruit', 'funny', 'ghost', 'glass', 'grass', 'green', 'group', 'guess', 'guide', 'habit', 'happy', 'heart', 'hello', 'honey', 'honor', 'horse', 'hotel', 'house', 'human', 'humor', 'icons', 'image', 'inbox', 'index', 'input', 'issue', 'jelly', 'jewel', 'jokes', 'judge', 'juice', 'juicy', 'knife', 'laugh', 'layer', 'learn', 'lemon', 'level', 'light', 'logic', 'lucky', 'lunch', 'lungs', 'major', 'maple', 'match', 'medal', 'metal', 'model', 'money', 'month', 'moral', 'motor', 'mouth', 'movie', 'music', 'nails', 'night', 'ninja', 'noise', 'north', 'notes', 'nurse', 'ocean', 'offer', 'olive', 'opera', 'orbit', 'order', 'organ', 'other', 'ought', 'owner', 'paint', 'panic', 'paper', 'parks', 'party', 'pasta', 'pause', 'peace', 'peach', 'pearl', 'phase', 'phone', 'piece', 'pilot', 'pitch', 'pixel', 'pizza', 'place', 'plane', 'plant', 'plate', 'point', 'pound', 'power', 'press', 'price', 'pride', 'prize', 'proof', 'prove', 'puppy', 'queen', 'quiet', 'quote', 'radio', 'raise', 'ranch', 'range', 'rapid', 'ratio', 'razor', 'react', 'relax', 'reply', 'retro', 'right', 'river', 'robot', 'roses', 'round', 'route', 'rugby', 'salad', 'sauce', 'scene', 'scope', 'score', 'seals', 'seeds', 'sense', 'seven', 'shape', 'share', 'shark', 'sharp', 'sheep', 'sheet', 'shift', 'shine', 'shirt', 'shock', 'shoes', 'sight', 'silly', 'skill', 'sleep', 'smile', 'smoke', 'snake', 'solve', 'sound', 'south', 'space', 'speed', 'spend', 'spice', 'spicy', 'spite', 'sport', 'squad', 'staff', 'stage', 'start', 'state', 'steam', 'steel', 'stock', 'stone', 'store', 'storm', 'stove', 'straw', 'study', 'stuff', 'sugar', 'suits', 'super', 'sushi', 'swear', 'sweat', 'sweet', 'swing', 'sword', 'syrup', 'table', 'tales', 'tasty', 'taxes', 'teams', 'tears', 'texts', 'theme', 'there', 'thick', 'thing', 'throw', 'thumb', 'title', 'today', 'token', 'tooth', 'total', 'touch', 'tower', 'toxic', 'track', 'trade', 'train', 'trees', 'trend', 'trial', 'tribe', 'trust', 'truth', 'twice', 'twist', 'uncle', 'union', 'unity', 'vague', 'valid', 'value', 'vapor', 'veins', 'verse', 'video', 'views', 'virus', 'visit', 'voice', 'voter', 'wages', 'wagon', 'waste', 'watch', 'water', 'weird', 'where', 'which', 'while', 'whole', 'whose', 'wings', 'woman', 'world', 'worry', 'wrath', 'write', 'wrote', 'yacht', 'years', 'yeast', 'youth', 'yummy']

# # ,''
# (print)
# # checking for duplicates
# def has_duplicates(word_list):
#     if len(word_list) != len(set(word_list)):
#         return True
#     else:
#         return False
# print(has_duplicates(word_list))

# prints word_list in alphabetical order
# print(sorted(word_list))

# # # shuffles the word_list
# random.shuffle(word_list)
# print(word_list)