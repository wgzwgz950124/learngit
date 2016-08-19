#! /usr/bin/env python
#coding=utf-8
import requests
import re
from lxml import etree
class gpa:
	def get(self,username,password):
		# username = input('请输入学号')
		# password = input('请输入密码')
		result = requests.Session()
		hea = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
		'Referer': 'http://urpjw.cau.edu.cn/loginAction.do'}
		url = 'http://urpjw.cau.edu.cn/loginAction.do'
		data = {'zjh1':'', 'tips':'', 'lx':'', 'evalue': '', 'eflag': '', 'zjh':username, 'mm':password }
		r1 = result.post(url, data=data, headers = hea)	
		hea1 = {'Referer':'http://urpjw.cau.edu.cn/gradeLnAllAction.do?type=ln&oper=sx',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
		url2 = 'http://urpjw.cau.edu.cn/gradeLnAllAction.do?type=ln&oper=sxinfo&lnsxdm=001'
		r = result.get(url2, headers = hea1)
		pattern1 = re.compile('<td align="center">.*?\s(\d{1}\.\d{1}).*?<p.*?>(.*?)&nbsp', re.S)
		list1 = re.findall(pattern1, r.text)
		pattern2 = re.compile('<td align="center">.*?[a-z]+.*?</td>.*?<td.*?\s(\d{1})\s.*?<p.*?>(.*?)&nbsp', re.S)
		list2 = re.findall(pattern2, r.text)
		grade = []
		xuefen= []
		for item1 in list1:
			grade.append(item1[1])
		for item2 in list2:
			grade.append(item2[1])
		for a1 in list1:
			xuefen.append(a1[0])
		for a2 in list2:
			xuefen.append(a2[0])
		return grade,xuefen
		
	def huoquf(self, b):
		txuefen = []
		xuefen = map(lambda x: float(x), b[1])
		for i in xuefen:
			txuefen.append(i)
		return txuefen
	def huoqug(self, b):
		tfengrade = []
		change = {'优秀':'95','中等':'75', '良好':'85','及格':'65','不及格':'59'}
		fengrade = [change[x] if x in change else x for x in b[0]]		
		fengrade = map(lambda x:float(x), fengrade)
		for i in fengrade:
			tfengrade.append(i)
		return tfengrade
	def getgpa(self,fengrade):
		tgradegpa = []
		def xuanze(x):
			if x > 89:
				return 4.0
			elif x > 84:
				return 3.7
			elif x > 81:
				return 3.3
			elif x > 77:
				return 3.0
			elif x > 74:
				return 2.7
			elif x > 71:
				return 2.3
			elif x > 67:
				return 2.0
			elif x > 63:
				return 1.5
			elif x > 59:
				return 1.0
			else:
				return 0 
		gpagrade = map(xuanze, fengrade)
		for i in gpagrade:
			tgradegpa.append(i)
		return tgradegpa
	def sumxuefen(self, xuefen):
		sumxuefen = sum(xuefen)
		return sumxuefen
	def caculategpa(self, gpagrade, xuefen, sumxuefen):
		prod1 = [ x * y for x, y in zip(gpagrade, xuefen)]
		allgpa = sum(prod1)
		avergpa = allgpa / sumxuefen
		print('您的GPA是%s' % avergpa)
		return avergpa
	def caculatefen(self, fengrade, xuefen, sumxuefen):
		prod = [ x * y for x, y in zip(fengrade, xuefen)]
		allfen = sum(prod)
		avergfen = allfen / sumxuefen
		print('您的加权平均分是%s' % avergfen)
		return avergfen
	def main(self, username, password):
		lists = []
		a = self.get(username, password)
		xuefen = self.huoquf(a)
		fengrade = self.huoqug(a)
		gpagrade = self.getgpa(fengrade)
		sumxuefen = self.sumxuefen(xuefen)
		num = self.caculategpa(gpagrade,xuefen,sumxuefen)
		num1 = self.caculatefen(fengrade,xuefen,sumxuefen)
		lists.append(num)
		lists.append(num1)
		print(lists)
		return lists
		
	# def main1(self, username, password):
	# 	a = self.get(username, password)
	# 	xuefen = self.huoquf(a)
	# 	fengrade = self.huoqug(a)
	# 	gpagrade = self.getgpa(fengrade)
	# 	sumxuefen = self.sumxuefen(xuefen)
	# 	num = self.caculatefen(gpagrade,xuefen,sumxuefen)
	# 	num1 = self.caculatefen(fengrade,xuefen,sumxuefen)
	# 	return num , num1
		# bb = self.caculatefen(fengrade,xuefen,sumxuefen)
# pp = gpa()
# pp.main(username, password)

