from hdwallet import HDWallet, cryptocurrencies
from hdwallet.utils import generate_mnemonic

class Wallets:
    def __init__(self):
        self.passphrase = None # "meherett"
        self.mnemonic = generate_mnemonic(language="english", strength=128)
        self.out = {
        'mnemonic': self.mnemonic,
        'btc': {
            'bip44': {
                'wif': '',
                'private_key': '',
                'address': {
                    'p2pkh': '',
                    'p2sh': '',
                    'p2wpkh': '',
                    'p2wpkh_in_p2sh': '',
                    'p2wsh': '',
                    'p2wsh_in_p2sh': ''
                },
            },
            'bip84': {
                'wif': '',
                'private_key': '',
                'address': {
                    'p2wpkh': '',
                    'p2pkh': '',
                    'p2sh': '',
                    'p2wpkh_in_p2sh': '',
                    'p2wsh': '',
                    'p2wsh_in_p2sh': ''
                },
            },
            'bip49': {
                'wif': '',
                'private_key': '',
                'address': {
                    'p2wpkh_in_p2sh': '',
                    'p2pkh': '',
                    'p2sh': '',
                    'p2wpkh': '',
                    'p2wsh': '',
                    'p2wsh_in_p2sh': ''
                },
            },

        },#end btc
        'eth':{
            'private_key': '',
            'address': ''
        }
    }

    def G(self):
        btc_44_wallet: HDWallet = HDWallet(cryptocurrency=cryptocurrencies.BitcoinMainnet)
        btc_44_wallet.from_mnemonic(mnemonic=self.mnemonic, passphrase=self.passphrase)
        btc_44_wallet.from_index(44, hardened=True)
        btc_44_wallet.from_index(0, hardened=True)
        btc_44_wallet.from_index(0, hardened=True)

        btc_44_wallet.from_index(0)
        btc_44_wallet.from_index(0)

        self.out['btc']['bip44']['private_key'] = btc_44_wallet.private_key()
        self.out['btc']['bip44']['wif'] = btc_44_wallet.wif()

        self.out['btc']['bip44']['address']['p2pkh'] = btc_44_wallet.p2pkh_address()
        self.out['btc']['bip44']['address']['p2sh'] = btc_44_wallet.p2sh_address()
        self.out['btc']['bip44']['address']['p2wpkh'] = btc_44_wallet.p2wpkh_address()
        self.out['btc']['bip44']['address']['p2wpkh_in_p2sh'] = btc_44_wallet.p2wpkh_in_p2sh_address()
        self.out['btc']['bip44']['address']['p2wsh'] = btc_44_wallet.p2wsh_address()
        self.out['btc']['bip44']['address']['p2wsh_in_p2sh'] = btc_44_wallet.p2wsh_in_p2sh_address()

        btc_84_wallet: HDWallet = HDWallet(cryptocurrency=cryptocurrencies.BitcoinMainnet)
        btc_84_wallet.from_mnemonic(mnemonic=self.mnemonic, passphrase=self.passphrase)
        btc_84_wallet.from_index(84, hardened=True)
        btc_84_wallet.from_index(0, hardened=True)
        btc_84_wallet.from_index(0, hardened=True)
        btc_84_wallet.from_index(0)
        btc_84_wallet.from_index(0)

        self.out['btc']['bip84']['private_key'] = btc_84_wallet.private_key()
        self.out['btc']['bip84']['wif'] = btc_84_wallet.wif()

        self.out['btc']['bip84']['address']['p2wpkh'] = btc_84_wallet.p2wpkh_address()
        self.out['btc']['bip84']['address']['p2pkh'] = btc_84_wallet.p2pkh_address()
        self.out['btc']['bip84']['address']['p2sh'] = btc_84_wallet.p2sh_address()
        self.out['btc']['bip84']['address']['p2wpkh_in_p2sh'] = btc_84_wallet.p2wpkh_in_p2sh_address()
        self.out['btc']['bip84']['address']['p2wsh'] = btc_84_wallet.p2wsh_address()
        self.out['btc']['bip84']['address']['p2wsh_in_p2sh'] = btc_84_wallet.p2wsh_in_p2sh_address()

        btc_49_wallet: HDWallet = HDWallet(cryptocurrency=cryptocurrencies.BitcoinMainnet)
        btc_49_wallet.from_mnemonic(mnemonic=self.mnemonic, passphrase=self.passphrase)
        btc_49_wallet.from_index(49, hardened=True)
        btc_49_wallet.from_index(0, hardened=True)
        btc_49_wallet.from_index(0, hardened=True)
        btc_49_wallet.from_index(0)
        btc_49_wallet.from_index(0)

        self.out['btc']['bip49']['private_key'] = btc_49_wallet.private_key()
        self.out['btc']['bip49']['wif'] = btc_49_wallet.wif()

        self.out['btc']['bip49']['address']['p2wpkh_in_p2sh'] = btc_49_wallet.p2wpkh_in_p2sh_address()
        self.out['btc']['bip49']['address']['p2pkh'] = btc_49_wallet.p2pkh_address()
        self.out['btc']['bip49']['address']['p2sh'] = btc_49_wallet.p2sh_address()
        self.out['btc']['bip49']['address']['p2wpkh'] = btc_49_wallet.p2wpkh_address()
        self.out['btc']['bip49']['address']['p2wsh'] = btc_49_wallet.p2wsh_address()
        self.out['btc']['bip49']['address']['p2wsh_in_p2sh'] = btc_49_wallet.p2wsh_in_p2sh_address()


        ethwallet: HDWallet = HDWallet(cryptocurrency=cryptocurrencies.EthereumMainnet)
        ethwallet.from_mnemonic(mnemonic=self.mnemonic, passphrase=self.passphrase)
        ethwallet.from_index(44, hardened=True)
        ethwallet.from_index(60, hardened=True)
        ethwallet.from_index(0, hardened=True)
        ethwallet.from_index(0)
        ethwallet.from_index(0)
        ethwallet.private_key()

        self.out['eth']['private_key'] = ethwallet.private_key()
        self.out['eth']['address'] = ethwallet.p2pkh_address()

    def get_info(self):
        return self.out