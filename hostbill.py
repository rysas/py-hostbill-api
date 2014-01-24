"""
=====================================================
 HostBill JSON API Python Library
=====================================================
:Info: See <http://api.hostbillapp.com/> for API implementation.
:Author: Damian Miller <miller.damian.c@gmail.com>
:Website: <http://www.github.com/rysas>
:Description: Python library for interfacing with HostBill <http://hostbillapp.com/>
"""
import requests

class HostBillHandler(object):
	def __init__(self, url, api_id, api_key, callable, call=''):
		self.url = url
		self.api_id = api_id
		self.api_key = api_key
		self.call = call

		self.callable = callable
			
	def __call__(self, *args, **kwargs):	
		kwargs.update({'outputformat':'json','api_id':self.api_id,'api_key':self.api_key,'call':self.call})
		for arg in args:
			kwargs.update(arg)
		
		print kwargs
		response = requests.post(self.url, data=kwargs);
		
		try:
			response = response.json()
		except:
			return False
		
		return response
			
	def __getattr__(self, call):
		return self.callable(self.url, self.api_id, self.api_key, self.callable, call)
 
class HostBill(HostBillHandler):
	pass
