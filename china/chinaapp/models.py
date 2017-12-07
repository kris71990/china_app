from django.db import models
import requests, bs4

class Region(models.Model):
    region_name = models.CharField(max_length=30)
    region_type = models.CharField(max_length=30)

class Province:
    
    def __init__(self, province):
        self.province = province
    
    def get_prov_info(self, province):
        res = requests.get('https://en.wikipedia.org/wiki/%s' % self.province)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        info_data = soup.select('.mergedrow td')
        info_head = soup.select('.mergedrow th')
        head_text = []
        data_text = []
        
        for each in info_head:
            entry = each.get_text()
            entry = entry.replace(u'\xa0', u'')
            entry = entry.replace(u'\u2022', u'')
            head_text.append(entry)
        for each in info_data:
            entry = each.get_text()
            entry = entry.replace(u'\xa0', u'')
            entry = entry.replace(u'/', u' ')
            entry = entry.replace(u'\n', u'; ')
            data_text.append(entry)
        
        zipped_list = zip(head_text, data_text)
        prov_dict = dict(zipped_list)
        return prov_dict

    def get_wiki(self, province):
        wiki = 'https://en.wikipedia.org/wiki/' + province
        return wiki

class Adm_reg(Province):

    def get_adm_reg_info(self, province):
        res = requests.get('https://www.cia.gov/library/publications/the-world-factbook/geos/hk.html')
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        info_data = soup.select('.category_data')
        info_head = soup.select('#field')
        head_text = []
        data_text = []
        
        for each in info_head:
            entry = each.get_text()
            """entry = entry.replace(u'\xa0', u'')
            entry = entry.replace(u'\u2022', u'')
            entry = entry.replace(u'\n', u'')"""
            head_text.append(entry)
        for each in info_data:
            entry = each.get_text()
            """entry = entry.replace(u'\xa0', u'')
            entry = entry.replace(u'/', u' ')
            entry = entry.replace(u'\n', u' ')"""
            data_text.append(entry)
        
        zipped_list = zip(head_text, data_text)
        adm_reg_dict = dict(zipped_list)
        return adm_reg_dict

class Aut_reg(Province):

    def get_aut_reg_info(self, province):
        res = requests.get('https://en.wikipedia.org/wiki/%s' % self.province)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        info_data = soup.select('.mergedrow td')
        info_head = soup.select('.mergedrow th')
        head_text = []
        data_text = []
        
        for each in info_head:
            entry = each.get_text()
            entry = entry.replace(u'\xa0', u'')
            entry = entry.replace(u'\u2022', u'')
            head_text.append(entry)
        for each in info_data:
            entry = each.get_text()
            entry = entry.replace(u'\xa0', u'')
            entry = entry.replace(u'/', u' ')
            entry = entry.replace(u'\n', u'; ')
            data_text.append(entry)
        
        zipped_list = zip(head_text, data_text)
        aut_reg_dict = dict(zipped_list)
        return aut_reg_dict

class Municipality(Province):

    def get_muni_info(self, province):
        res = requests.get('https://en.wikipedia.org/wiki/%s' % self.province)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        info_data = soup.select('.mergedrow td')
        info_head = soup.select('.mergedrow th')
        head_text = []
        data_text = []
        
        for each in info_head:
            entry = each.get_text()
            entry = entry.replace(u'\xa0', u'')
            entry = entry.replace(u'\u2022', u'')
            head_text.append(entry)
        for each in info_data:
            entry = each.get_text()
            entry = entry.replace(u'\xa0', u'')
            entry = entry.replace(u'/', u' ')
            entry = entry.replace(u'\n', u'; ')
            data_text.append(entry)
        
        zipped_list = zip(head_text, data_text)
        muni_dict = dict(zipped_list)
        return muni_dict

class Taiwan(Province):

    def __init__(self, province):
        self.province = province
    
    def get_prov_info(self, province):
        res = requests.get('https://en.wikipedia.org/wiki/%s' % self.province)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        info_data = soup.select('.infobox geography vcard td')
        info_head = soup.select('.infobox geography vcard th')
        head_text = []
        data_text = []
        
        for each in info_head:
            entry = each.get_text()
            entry = entry.replace(u'\xa0', u'')
            entry = entry.replace(u'\u2022', u'')
            head_text.append(entry)
        for each in info_data:
            entry = each.get_text()
            entry = entry.replace(u'\xa0', u'')
            entry = entry.replace(u'/', u' ')
            entry = entry.replace(u'\n', u'; ')
            data_text.append(entry)
        
        zipped_list = zip(head_text, data_text)
        prov_dict = dict(zipped_list)
        return prov_dict






