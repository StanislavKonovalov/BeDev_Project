# Уровни сложности
levels = {
    "Beginner": 1,
    "Medium": 2,
    "Expert": 3
}

Beginner = levels.get("Beginner")
Medium = levels.get("Medium")
Expert = levels.get("Expert")

# Переменные чат-бота
bot_name = "English Bot"

# Пользователь
user = {
    'user_name': 'Stas',
    'user_id': "000001",
    'user_bot': False,
    'user_level': Medium,
    'user_text': "love"
}


# Предложения от чат-бота
bot_sentence_1 = {
    "bot_sentence": "I love England!",
    "user_level": Beginner
}

bot_sentence_2 = {
    "bot_sentence": "When my time comes \n Forget the wrong that I’ve done.",
    "user_level": Medium
}

bot_sentence_3 = {
    "bot_sentence": "Such people eventually succeed, sometimes through persistence, but often through the unconditional love and support of others.",
    "user_level": Expert
}

bot_sentence_4 = {
    "bot_sentence": "In a hole in the ground there lived a hobbit.",
    "user_level": Beginner
}

bot_sentence_5 = {
    "bot_sentence": "The sky the port was the color of television, tuned to a dead channel.",
    "user_level": Medium
}

bot_sentence_6 = {
    "bot_sentence": "The man in black fled across the desert, and the gunslinger followed.",
    "user_level": Expert
}

bot_sentence_7 = {
    "bot_sentence": "The Consul watched as Kassad raised the death wand.",
    "user_level": Beginner
}

bot_sentence_8 = {
    "bot_sentence": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore",
    "user_level": Medium
}

bot_sentence_9 = {
    "bot_sentence": "I learned very early the difference between knowing the name of something and knowing something.",
    "user_level": Expert
}

bot_sentences = [bot_sentence_1, 
bot_sentence_2, 
bot_sentence_3, 
bot_sentence_4, 
bot_sentence_5, 
bot_sentence_6, 
bot_sentence_7, 
bot_sentence_8, 
bot_sentence_9]

user_lvl = user.get("user_level")
user_message = user.get("user_text")


# Объявляем функцию подбора предложений
def search_sentence(level: int = None, message: str = None, sentences: list = None):
    matched_sentences = []
    result_message = ""

    for x in sentences:
        # sentences_lvl = x.get("user_level")
        sentences_txt = x.get("bot_sentence")
        # if sentences_lvl <= level:
        if message in sentences_txt:
            matched_sentences.append(sentences_txt)

    if len(matched_sentences) == 0:
        result_message = "We did not find a suitable sentense"
    if len(matched_sentences) == 1:
        result_message = matched_sentences[0]
    if len(matched_sentences) > 1:
        for y in matched_sentences:
            result_message += "\n...\n" + y + "\n...\n"

    return result_message

