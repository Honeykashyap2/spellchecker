from textblob import TextBlob
class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
    def correct_spell(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)
if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "appple"
    print(obj.correct_spell(message))
   







