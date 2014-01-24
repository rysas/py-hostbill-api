import hostbill

hb = hostbill.HostBill('http://my.hostbillendpoint.com/admin/api.php', 'MYAPIID', 'MYAPIKEY', hostbill.HostBillHandler)

client_details = hb.getClientDetails({id:8})

if client_details['success']:
	print client_details
else:
	print "I failed, sorry master :("
