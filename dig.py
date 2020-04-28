
#ECON435 HW1 Q3
#Author: Xiao FU
#UID:305448673

from lxml import etree
import json
import sys

# 'book.html'='ThriftBook1.html'

def parse_book_html(html):
    books_list = []
    with open(html, encoding='utf-8') as f:
        text = f.read()
    books_html = etree.HTML(text)
    script_nodes = books_html.xpath('//script')[9]
    info_str = script_nodes.text
    index = info_str.find("works")
    books_info = json.loads(info_str[index+8:-3])

    for book_info in books_info:
        tmp_book = dict.fromkeys(('title', 'price', 'format', 'condition', 'authors'), None)
        tmp_book['title'] = book_info.get('title', None)
        tmp_book['price'] = book_info.get('buyNowPrice', None)
        tmp_book['format'] = book_info.get('media', None)
        tmp_book['condition'] = book_info.get('qualityDescription', None)
        authors = book_info.get('authors')
        authors_name = None
        for author in authors:
            authors_name = author.get('authorName', None)
        tmp_book['authors'] = authors_name
        books_list.append(tmp_book)
    return books_list


def generate_xml(books_list, xml_name):
    f = open(xml_name, 'w')
    f.writelines(['<?xml version="1.0"?>\n', '<books>\n'])
    count = 1
    for book in books_list:
        lines = ['\t<book>\n', '\t\t<id>' + str(count) + '</id>\n']
        for key, value in book.items():
            lines.append('\t\t' + '<' + key + '>' + str(value) + '</' + key + '>\n')
        lines.append('\t</book>\n')
        count += 1
        f.writelines(lines)
    f.write('</books>')
    f.close()


if __name__ == '__main__':
    
    html = 'book.html'
    xml_name = 'book.xml'
    books_list = parse_book_html(html)
    generate_xml(books_list, xml_name)







