from project import Fetch_Info

def main():
    test_fetch_word_title()
    test_fetch_word_definations()
    test_fetch_word_Antonyms()
    test_fetch_word_Antonyms()


def test_fetch_word_title():
    fetch_info = Fetch_Info()
    assert fetch_info.fetch_word_title("word") == "word"

def test_fetch_word_definations():
    fetch_info = Fetch_Info()
    assert fetch_info.fetch_word_definations("gratitude") == ['The state of being grateful.']

def test_fetch_word_Synonyms():
    fetch_info = Fetch_Info()
    assert fetch_info.fetch_word_Synonyms("gratitude") == ['appreciation', 'thanks', 'appreciativeness', 'thankfulness', 'gratefulness', 'acknowledgement', 'satisfaction', 'thanksgiving', 'indebtedness', 'acknowledgment', 'gratification', 'recognition', 'tribute', 'appreciation', 'thanks', 'appreciativeness', 'thankfulness', 'gratefulness', 'acknowledgement', 'satisfaction', 'thanksgiving', 'indebtedness', 'acknowledgment', 'gratification', 'recognition', 'tribute']

def test_fetch_word_Antonyms():
    fetch_info = Fetch_Info()
    assert fetch_info.fetch_word_Antonyms("gratitude") == ['ingratitude', 'ungratefulness', 'thanklessness', 'unappreciation', 'ingratitude', 'ungratefulness', 'thanklessness', 'unappreciation']