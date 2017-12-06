import vk_api
vkontakte = vk_api.VkApi(token='8b4e4e35b0dc2c582ca98f57b13bb67b06ebe79e4929a2dfed75058060e0284d50422ea733e97d99930fb')
vkontakte._auth_token()
values = {'out': 0, 'count': 100, 'time_offset': 60}

def write_msg(user_id, s):
    vkontakte.method('messages.send', {'user_id': user_id, 'message': s})


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


while True:
    response = vkontakte.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
        text = response['items'][0]['body']
        if is_ascii(text):
            write_msg(item['user_id'], 'Ваш текст не является кириллицей')
        elif response['items'][0]['body'] == 'ь':
            write_msg(item['user_id'], 'Эти буквы не переводятся')
        elif response['items'][0]['body'] == 'Ь':
            write_msg(item['user_id'], 'Эти буквы не переводятся')
        elif response['items'][0]['body'] == 'Ъ':
            write_msg(item['user_id'], 'Эти буквы не переводятся')
        elif response['items'][0]['body'] == 'ъ':
            write_msg(item['user_id'], 'Эти буквы не переводятся')
        else:
            final = text.replace("я","i'a").replace("Я","I'a").replace("ю","i'y").replace("Ю","I'y").replace("ц","ts").replace("а", "a").replace("ә", "a'").replace("б", "b").replace("д", "d").replace("е",
                                                                                                                                                                                                    "e").replace(
            "ф", "f").replace("г", "g").replace("ғ", "g'").replace("х", "h").replace("һ", "h").replace("і",
                                                                                                       "i").replace(
            "и", "i'").replace("й", "i'").replace("ж", "j").replace("к", "k").replace("л", "l").replace("м",
                                                                                                        "m").replace(
            "н", "n").replace("ң", "n'").replace("о", "o").replace("ө", "o'").replace("п", "p").replace("қ",
                                                                                                        "q").replace(
            "р", "r").replace("с", "s").replace("ш", "s'").replace("щ", "s'").replace("ч", "c'").replace("т",
                                                                                                         "t").replace(
            "ұ", "u").replace("ү", "u'").replace("в", "v").replace("ы", "y").replace("у", "y'").replace("з",
                                                                                                        "z").replace(
            "ь", "").replace("ъ", "").replace("Ъ", "").replace("Ь", "").replace("А", "A").replace("Ә", "A'").replace("Б", "B").replace("Д",
                                                                                                                                       "D").replace(
            "Е", "E").replace("Ф", "F").replace("Г", "G").replace("Ғ", "G'").replace("Х", "H").replace("І",
                                                                                                       "I").replace(
            "Й", "I'").replace("И", "I'").replace("Ж", "J").replace("К", "K").replace("Л", "L").replace("М",
                                                                                                        "M").replace(
            "Н", "N").replace("Ң", "N'").replace("О", "O").replace("Ө", "O'").replace("П", "P").replace("Қ",
                                                                                                        "Q").replace(
            "Р", "R").replace("С", "S").replace("Ш", "S'").replace("Щ", "S'").replace("Ч", "C'").replace("Т",
                                                                                                         "T").replace(
            "Ұ", "U").replace("Ү", "U'").replace("В", "V").replace("Ы", "Y").replace("У", "Y'").replace("З", "Z").replace("ё", "е").replace("Ё", "E").replace("э","e").replace("Э","E")
            write_msg(item['user_id'], final)


