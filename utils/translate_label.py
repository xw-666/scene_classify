from googletrans import Translator
from time import sleep

translator = Translator(service_urls=['translate.google.cn'])

input_file = '../model_data/categories_places365.txt'
output_file = '../model_data/cn_categories_places365.txt'
en_label_file = open( input_file, 'r')
cn_label_file = open( output_file, 'w')
cn_list = []
for line in en_label_file.readlines():
    sleep(1)
    label_num = line.split(' ')[1]
    label_part = line.split(' ')[0]
    en_latter = label_part.split('/')[1]
    en_word = label_part.split('/')[2].replace('_', ' ')
    print( en_word)
    cn_word = translator.translate(en_word, src='en', dest='zh-cn').text
    cn_line = '/' + en_latter + '/' + cn_word + '(' + en_word.replace(' ', '_') + ')' + ' ' + label_num
    cn_label_file.write( cn_line)