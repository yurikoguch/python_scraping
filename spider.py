from lxml import etree, html
import xlsxwriter
import pandas as pd



parser = etree.HTMLParser()
tree = etree.parse("C:/Users/ПК/prod_pyth/index.html.html", parser)
a = []
b = []
c = []
d = []
e = []

Name = tree.xpath('//div[@class="cls_026"]/span/text()')
Afiliation_name = tree.xpath('//div[@class="cls_028"]/span[@class="cls_029"]/text()')
Session_name = tree.xpath('//div[@class="cls_033"]/span/text()')
Topic_title = tree.xpath('//div[@class="cls_025"]/span/text()')
Presentacion_abstract = tree.xpath('//div[@class="cls_030"]/span[@class="cls_031"][1]/text()')

a.append (Name)
b.append (Afiliation_name)
c.append (Session_name)
d.append (Topic_title)
e.append (Presentacion_abstract)


df = pd.DataFrame({'Name': a, 'Afiliation name': b, 'Session name': c, 'Topic title': d, 'Presentacion abstract': e })
writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')

writer.save()





                

                


