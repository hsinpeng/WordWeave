from PyMultiDictionary import MultiDictionary
from utils import (chinese_conversion)

def main():
    run_option = 0
    dict_lang = "en"
    trans_lang = "zh"
    print("Hello from WordWeave!")
    try:
        match run_option:
            case 0:
                word = "nonchalant"
                dictionary = MultiDictionary()
                # meaning = dictionary.meaning('en', 'good', dictionary=DICT_MW)
                meaning = dictionary.meaning(dict_lang, word)
                print(f"----------------- {dict_lang}:{word} -----------------")
                if meaning[0]:
                    print(f"word_type: {meaning[0]}")
                    print("----------------------------------")
                    print(f"word_meaning: {meaning[1]}")
                    print("----------------------------------")
                    print(f"word_wikipedia: {meaning[2]}")
                    print("----------------------------------")
                else:
                    print(f"cannot find '{word}' in {dict_lang} dictionary.")

                synonym = dictionary.synonym(dict_lang, word)
                print(f"----------------- Synonym of '{word}' in {dict_lang} -----------------")
                if synonym:
                    print(synonym)
                else:
                    print(f"cannot find synonym of '{word}' in {dict_lang} dictionary.")

                antonym = dictionary.antonym(dict_lang, word)
                print(f"----------------- Antonym of '{word}' in {dict_lang} -----------------")
                if antonym:
                    print(antonym)
                else:
                    print(f"cannot find antonym of '{word}' in {dict_lang} dictionary.")

                translations = dictionary.translate(dict_lang, word) # This will translate the word to over 20 languages
                # translations = dictionary.translate(dict_lang, word, to=tran) # This will translate word to 'tran' (if Google API is available)
                print(f"----------------- Translate '{word}' from {dict_lang} to {trans_lang} -----------------")
                if translations:
                    for translation in translations:
                        if translation[0] == trans_lang:
                            print(f"Translate: {chinese_conversion(translation[1])}")
                    print("----------------------------------")
                else:
                    print(f"cannot find '{word}' in {dict_lang} dictionary.")

            case 1:
                words = ['hotel', 'ambush', 'nonchalant', 'perceptive']
                dictionary = MultiDictionary(*words)
                dictionary.set_words_lang(dict_lang) # All words are English
                print(f"----------------- Batch of {words} -----------------")
                meanings = dictionary.get_meanings() # This print the meanings of all the words
                synonyms = dictionary.get_synonyms() # Get synonyms list
                antonyms = dictionary.get_antonyms() # Get antonyms
                translations = dictionary.get_translations() # This will translate all words to over 20 languages
                #translations_google = dictionary.get_translations(to=tran) # This will translate all words to 'tran' (if Google API is available)
                index = 0
                for word in words:
                    print(f"----- Results of '{word}' -----")
                    print(f"Meaning: {meanings[index]}")
                    print(f"-----------------------------")
                    print(f"Synonym: {synonyms[index]}")
                    print(f"-----------------------------")
                    print(f"Antonym: {antonyms[index]}")
                    print(f"-----------------------------")
                    for translation in translations[index]:
                        if translation[0] == trans_lang:
                            print(f"Translate: {chinese_conversion(translation[1])}")
                    print(f"-----------------------------\n\n")
                    index += 1

            case 2:
               cht_words = "總裁乾了那杯乾淨的酒，交代秘書要把乾貨和頭髮分類好，然後繼續幹活。" 
               chs_words = "总裁干了那杯干净的酒，交代秘书要把干货和头发分类好，然后继续干活。" 
               print(f"TW-TW conversion: {chinese_conversion(cht_words)}")
               print(f"-----------------------------")
               print(f"TW-CN conversion: {chinese_conversion(cht_words, target="CN")}")
               print(f"-----------------------------")
               print(f"CN-CN conversion: {chinese_conversion(chs_words, target="CN")}")
               print(f"-----------------------------")
               print(f"CN-TW conversion: {chinese_conversion(chs_words)}")
               print(f"-----------------------------")
               print(f"CN-HK conversion: {chinese_conversion(chs_words, target="HK")}")
               print(f"-----------------------------")

            case _:
                print(f"Error: Unknown run_option ({run_option})!")

    except Exception as e:
        print(f"Unknown Error: {e}") 

    finally: # This ALWAYS runs, ensuring every resource is closed even if an error occurs
        pass

if __name__ == "__main__":
    main()