from web3 import Web3

proxy = input ("Введите URL прокси-сервера: http://")

w3 = Web3(Web3.HTTPProvider(
    'https://rpc.ankr.com/eth',
    request_kwargs={
        'proxies': {
            'http': proxy,
            'https': proxy,
        }
    } if proxy else {}
))

if w3.is_connected():
    print ("Есть коннект!")
else:
    print ("Нет коннекта!")

address = input ("Введите кошелек Metamask: ")
balance = w3.eth.get_balance(address)
ether_balance = w3.from_wei(balance, 'ether')
print(f"Баланс {address} равен {ether_balance}")
