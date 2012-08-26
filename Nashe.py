# coding: cp1251
import os,urllib2
import re,xlwt

font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.bold = True

style0 = xlwt.XFStyle()
style0.font = font0

wb = xlwt.Workbook(encoding='cp1251')
ws = wb.add_sheet('Новости музыки')
ws.write(0, 0, 'Тема', style0)
ws.write(0, 1, 'Новость', style0)

page = 1
a = 1
b = 1
while page < 23:
	url = 'http://www.nashe.ru/news/new_music/?PAGEN_2=' + str(page)

	html = urllib2.urlopen(url).read()
	re1 = '<h3><a href="/news/new_music/.+</a></h3>'
	titles = re.findall(re1,html)
	for title in titles:
		text = re.sub('<[^>]+>','',title)
		print text.decode('cp1251').encode('cp866','xmlcharrefreplace')
		ws.write(a, 0, str(text))
		a += 1
		
	re2 = '<p>.+подробнее</a></p>'
	contents = re.findall(re2,html)
	for content in contents:
		text = re.sub('<[^>]+>','',content)
		text = re.sub('подробнее', '', text)
		print text.decode('cp1251').encode('cp866','xmlcharrefreplace')
		ws.write(b, 1, str(text))
		b += 1
	
	page += 1

wb.save('info.xls')