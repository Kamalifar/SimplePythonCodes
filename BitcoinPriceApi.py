import cryptocompare

cryptocompare.cryptocompare._set_api_key_parameter('api_key_from_cryptocompare_it is free')

response=cryptocompare.get_price('BTC', currency='USD')

print (response['BTC']['USD'])