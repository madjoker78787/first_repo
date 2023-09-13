from bs4 import BeautifulSoup
import requests
from GW import Wallets as Wall
import time
import asyncio

async def check_btc(arr: dict):
    address = ""
    for i in arr['btc']['bip44']['address'].values():
        address += f"{i}|"
    for i in arr['btc']['bip49']['address'].values():
        address += f"{i}|"
    for i in arr['btc']['bip84']['address'].values():
        address += f"{i}|"
    try:
        request = requests.get(
            f"https://blockchain.info/multiaddr?active={address}", timeout=15)
        if request.status_code == 200:
            answer = request.json()
            for row in answer['addresses']:
                if row["final_balance"] > 0 or row['n_tx'] > 0 or row['total_received'] > 0 or row['total_sent'] > 0:
                    with open(f"D:\\PYTHON2\\CHECK\\1.txt", 'a') as f:
                    #with open(f"D:\\PYTHON\\TWO\\etherscan\\1.txt", 'a') as f:
                        f.write(f"{arr['btc']}")
                #else:
                #    print(f"BTC -- {row['address']} пустой")
        else:
            print(f"{request.status_code}")
            await asyncio.sleep(60)
    except:
        pass



async def check_eth(arr: dict) -> None:
    blockscan_bool = False
    balance_bool = False
    tokens_bool = False
    url = f"https://etherscan.io/address/{arr['eth']['address']}"

    headers = {
        'Content-Type': 'text/html; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
    }

    page = requests.get(url, headers=headers)

    if page.status_code == 200:
        print(page.status_code)
        soup = BeautifulSoup(page.text, "html.parser")

        # blockscan
        try:
            blockscan1 = soup.findAll('div', class_='d-flex flex-wrap align-items-center gap-1')
            blockscan2 = blockscan1[1].text.strip().split(' ')

            if blockscan2[0].isdigit():
                # print(f"blockscan {blockscan2[0]}")
                # print(f"blockscan - {result}")
                blockscan_bool = True
            else:
                pass
        except:
            pass

        # balance
        try:
            balance1 = soup.select("div > div > div")
            balance2 = balance1[32].text.split(' ')

            if float(balance2[0].strip()) > 0:
                balance_bool = True
                # print(f"balance {float(balance2[0].strip())}")
                # print(f"balance - {result}")
        except:
            pass

        # count tokens
        try:
            token = soup.findAll('span', class_='small text-muted')

            print(f"tokens {token[2].text.strip('()')}")
            tokens_bool = True

        except:
            pass
        if blockscan_bool or balance_bool or tokens_bool:
            print(arr)
            with open(f"D:\\PYTHON2\\CHECK\\{arr['eth']['address']}.txt", 'x') as f:
                f.write(f'{arr}')
        #else:
        #    print(f"ETH -- {arr['eth']['address']} пустой")

    else:
        print(page.status_code)
        await asyncio.sleep(100)

async def main():
    while True:
        gen = Wall()
        gen.G()
        a = gen.get_info()
        eth_ = asyncio.create_task(check_eth(a))
        btc_ = asyncio.create_task(check_btc(a))
        await eth_
        await btc_
        await asyncio.sleep(4)


asyncio.run(main())