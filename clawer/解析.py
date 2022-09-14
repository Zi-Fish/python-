from lxml import etree

tree = etree.parse('解析.html')

# / 子节点 // 孙节点
li_list = tree.xpath('//body//li/text()')
print(li_list)
print(len(li_list))
