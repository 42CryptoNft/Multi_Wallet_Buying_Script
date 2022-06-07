## Multi Wallet Buying Script v0.9 by LordKrueger / Twitter @42CryptoNft

## Release Notes: v0.9
## - ContractAbi is now added automaticaly, only Contract adress has to be entered. Thanks @doyler
## - Further function has been implemented to directly Share Eth, wait defined Nr of Blocks and Mint, with one run of the script. Called "SaM"

## Realease Notes v0.85
## - First Creation 06/04/2022

import json
import requests
import time
from datetime import datetime
from web3 import Web3

## Enter your web3 Provider here (Alchemy, Infura or whatever you prefer):
## Change to Mainnet if you are done with testing!

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/pleaseReplace'))

## Please enter your Etherscan API Key

apiKey = "pleaseReplace"

## Enter the ChainID
## Mainnet = 1
## Ropsten = 3
## Rinkeby = 4
## Goerli  = 5

chainId = 1

##------------------------------------------------------------------------##
##------------------User Interface---Insert your Data here----------------##
##------------------------------------------------------------------------##

## Fill out those variables suitable for current contract

## ToolFunction:
## = "M1 - M20" to Mint 
## = "S1 - S20" to sent money from Main Wallet to Burner Wallets
## = "SaM1 - SaM20" to sent money to Burner Wallets, wait a specific amount of blocks and mint afterwards automatically

## maxMint = How many NFTs shall be minted from each wallet in one TX
## valueMint = Price of all NFT (for 1 Wallet) in one TX in ETH (be careful what you enter, overpaying is possible on some contracts)
## valueShare = Amount of ETH you want so sent to Burner Wallets
## mintVariable = Enter the name of the mint Function (e.g. mint, freemint, getxyz or whatever the name is in the contract you use)
## gasUsage = How much Gas does the transaction need (check previous TX on Etherscan)
## maxGasMint = maximum Gas your TX will use to Mint
## maxPrioMint = maximum Tip your TX will use to Mint
## maxGasShare = maximum Gas your TX will use to sent ETH to Burner Wallets
## maxPrioShare = maximum Tip your TX will use to sent ETH to Burner Wallets
## waitingBlocks = Only for "SaM function" - Number of Blocks to wait between sent and mint. 
## address = Contract Address

ToolFunction = "Test"

maxMint = 1
mintVariable = "mint"

valueMint = 0.00
valueShare = 0.00

gasUsage = 150000

maxGasShare = 35
maxPrioShare = 2

maxGasMint = 35
maxPrioMint = 2

waitingBlocks = 3

address = Web3.toChecksumAddress('pleaseReplace')

## Enter all your accounts here:

my_accountMain = Web3.toChecksumAddress("pleaseReplace")
private_keyMain ='pleaseReplace'
my_account1 = Web3.toChecksumAddress("pleaseReplace")
private_key1 ='pleaseReplace'
my_account2 = Web3.toChecksumAddress("pleaseReplace")
private_key2 ="pleaseReplace"
my_account3 = Web3.toChecksumAddress("pleaseReplace")
private_key3 ="pleaseReplace"
my_account4 = Web3.toChecksumAddress("pleaseReplace")
private_key4 ="pleaseReplace"
my_account5 = Web3.toChecksumAddress("pleaseReplace")
private_key5 ="pleaseReplace"
my_account6 = Web3.toChecksumAddress("pleaseReplace")
private_key6 ="pleaseReplace"
my_account7 = Web3.toChecksumAddress("pleaseReplace")
private_key7 ="pleaseReplace"
my_account8 = Web3.toChecksumAddress("pleaseReplace")
private_key8 ="pleaseReplace"
my_account9 = Web3.toChecksumAddress("pleaseReplace")
private_key9 ="pleaseReplace"
my_account10 = Web3.toChecksumAddress("pleaseReplace")
private_key10 ="pleaseReplace"
my_account11 = Web3.toChecksumAddress("pleaseReplace")
private_key11 ="pleaseReplace"
my_account12 = Web3.toChecksumAddress("pleaseReplace")
private_key12 ="pleaseReplace"
my_account13 = Web3.toChecksumAddress("pleaseReplace")
private_key13 ="pleaseReplace"
my_account14 = Web3.toChecksumAddress("pleaseReplace")
private_key14 ="pleaseReplace"
my_account15 = Web3.toChecksumAddress("pleaseReplace")
private_key15 ="pleaseReplace"
my_account16 = Web3.toChecksumAddress("pleaseReplace")
private_key16 ="pleaseReplace"
my_account17 = Web3.toChecksumAddress("pleaseReplace")
private_key17 ="pleaseReplace"
my_account18 = Web3.toChecksumAddress("pleaseReplace")
private_key18 ="pleaseReplace"
my_account19 = Web3.toChecksumAddress("pleaseReplace")
private_key19 ="pleaseReplace"
my_account20 = Web3.toChecksumAddress("pleaseReplace")
private_key20 ="pleaseReplace"

##------------------------------------------------------------------------##
## ----------------Below that point, intern stuff only -------------------##
## ------Only change things here if you know what you are doing ----------##
##------------------------------------------------------------------------##

abiEndpoint = "https://api.etherscan.io/api?module=contract&apikey=%s&action=getabi&address=%s" % (apiKey, address)

abi = requests.get(abiEndpoint).json()['result']

contract = w3.eth.contract(address=address, abi=abi)

nonceMain = w3.eth.getTransactionCount(my_accountMain)
nonce1 = w3.eth.getTransactionCount(my_account1)
nonce2 = w3.eth.getTransactionCount(my_account2)
nonce3 = w3.eth.getTransactionCount(my_account3)
nonce4 = w3.eth.getTransactionCount(my_account4)
nonce5 = w3.eth.getTransactionCount(my_account5)
nonce6 = w3.eth.getTransactionCount(my_account6)
nonce7 = w3.eth.getTransactionCount(my_account7)
nonce8 = w3.eth.getTransactionCount(my_account8)
nonce9 = w3.eth.getTransactionCount(my_account9)
nonce10 = w3.eth.getTransactionCount(my_account10)
nonce11 = w3.eth.getTransactionCount(my_account11)
nonce12 = w3.eth.getTransactionCount(my_account12)
nonce13 = w3.eth.getTransactionCount(my_account13)
nonce14 = w3.eth.getTransactionCount(my_account14)
nonce15 = w3.eth.getTransactionCount(my_account15)
nonce16 = w3.eth.getTransactionCount(my_account16)
nonce17 = w3.eth.getTransactionCount(my_account17)
nonce18 = w3.eth.getTransactionCount(my_account18)
nonce19 = w3.eth.getTransactionCount(my_account19)
nonce20 = w3.eth.getTransactionCount(my_account20)

Blocknumber = w3.eth.get_block_number()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def buy1():
    global tx_hash
    print ("Buy 1 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce1,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key1)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 1 finished")

def buy2():
    global tx_hash
    print ("Buy 2 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce2,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key2)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 2 finished")

def buy3():
    global tx_hash
    print ("Buy 3 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce3,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key3)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 3 finished")    

def buy4():
    global tx_hash
    print ("Buy 4 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce4,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key4)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 4 finished")

def buy5():
    global tx_hash
    print ("Buy 5 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce5,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key5)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 5 finished")

def buy6():
    global tx_hash
    print ("Buy 6 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce6,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key6)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 6 finished")

def buy7():
    global tx_hash
    print ("Buy 7 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce7,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key7)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 7 finished")

def buy8():
    global tx_hash
    print ("Buy 8 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce8,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key8)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 8 finished")

def buy9():
    global tx_hash
    print ("Buy 9 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce9,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key9)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 9 finished")

def buy10():
    global tx_hash
    print ("Buy 10 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce10,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key10)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 10 finished")

def buy11():
    global tx_hash
    print ("Buy 11 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce11,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key11)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 11 finished")

def buy12():
    global tx_hash
    print ("Buy 12 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce12,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key12)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 12 finished")

def buy13():
    global tx_hash
    print ("Buy 13 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce13,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key13)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 13 finished")

def buy14():
    global tx_hash
    print ("Buy 14 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce14,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key14)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 14 finished")

def buy15():
    global tx_hash
    print ("Buy 15 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce15,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key15)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 15 finished")

def buy16():
    global tx_hash
    print ("Buy 16 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce16,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key16)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 16 finished")

def buy17():
    global tx_hash
    print ("Buy 17 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce17,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key17)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 17 finished")

def buy18():
    global tx_hash
    print ("Buy 18 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce18,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key18)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 18 finished")

def buy19():
    global tx_hash
    print ("Buy 19 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce19,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key19)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 19 finished"),

def buy20():
    global tx_hash
    print ("Buy 20 started")
    my_tx = contract.get_function_by_name(mintVariable)(maxMint).buildTransaction(
    {
            "nonce": nonce20,
            "value": w3.toWei(valueMint, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasMint,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioMint,"gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(my_tx, private_key20)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Buy 20 finished")

def share1():
    global tx_hash
    print ("Share ETH to Wallet 1 started")
    my_tx = {
            "nonce": nonceMain,
            "to": my_account1,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 1 finished")

def share2():
    global tx_hash
    print ("Share ETH to Wallet 2 started")
    my_tx = {
            "nonce": nonceMain + 1,
            "to": my_account2,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 2 finished")

def share3():
    global tx_hash
    print ("Share ETH to Wallet 3 started")
    my_tx = {
            "nonce": nonceMain + 2,
            "to": my_account3,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 3 finished")

def share4():
    global tx_hash
    print ("Share ETH to Wallet 4 started")
    my_tx = {
            "nonce": nonceMain + 3,
            "to": my_account4,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 4 finished")

def share5():
    global tx_hash
    print ("Share ETH to Wallet 5 started")
    my_tx = {
            "nonce": nonceMain + 4,
            "to": my_account5,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 5 finished")

def share6():
    global tx_hash
    print ("Share ETH to Wallet 6 started")
    my_tx = {
            "nonce": nonceMain + 5,
            "to": my_account6,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 6 finished")

def share7():
    global tx_hash
    print ("Share ETH to Wallet 7 started")
    my_tx = {
            "nonce": nonceMain + 6,
            "to": my_account7,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 7 finished")

def share8():
    global tx_hash
    print ("Share ETH to Wallet 8 started")
    my_tx = {
            "nonce": nonceMain + 7,
            "to": my_account8,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 8 finished")

def share9():
    global tx_hash
    print ("Share ETH to Wallet 9 started")
    my_tx = {
            "nonce": nonceMain + 8,
            "to": my_account9,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 9 finished")

def share10():
    global tx_hash
    print ("Share ETH to Wallet 10 started")
    my_tx = {
            "nonce": nonceMain + 9,
            "to": my_account10,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 10 finished")

def share11():
    global tx_hash
    print ("Share ETH to Wallet 11 started")
    my_tx = {
            "nonce": nonceMain + 10,
            "to": my_account11,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 11 finished")

def share12():
    global tx_hash
    print ("Share ETH to Wallet 12 started")
    my_tx = {
            "nonce": nonceMain + 11,
            "to": my_account12,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 12 finished")

def share13():
    global tx_hash
    print ("Share ETH to Wallet 13 started")
    my_tx = {
            "nonce": nonceMain + 12,
            "to": my_account13,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 13 finished")

def share14():
    global tx_hash
    print ("Share ETH to Wallet 14 started")
    my_tx = {
            "nonce": nonceMain + 13,
            "to": my_account14,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 14 finished")

def share15():
    global tx_hash
    print ("Share ETH to Wallet 15 started")
    my_tx = {
            "nonce": nonceMain + 14,
            "to": my_account15,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 15 finished")

def share16():
    global tx_hash
    print ("Share ETH to Wallet 16 started")
    my_tx = {
            "nonce": nonceMain + 15,
            "to": my_account16,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 16 finished")

def share17():
    global tx_hash
    print ("Share ETH to Wallet 17 started")
    my_tx = {
            "nonce": nonceMain + 16,
            "to": my_account17,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 17 finished")

def share18():
    global tx_hash
    print ("Share ETH to Wallet 18 started")
    my_tx = {
            "nonce": nonceMain + 17,
            "to": my_account18,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 18 finished")

def share19():
    global tx_hash
    print ("Share ETH to Wallet 19 started")
    my_tx = {
            "nonce": nonceMain + 18,
            "to": my_account19,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 19 finished")

def share20():
    global tx_hash
    print ("Share ETH to Wallet 20 started")
    my_tx = {
            "nonce": nonceMain + 19,
            "to": my_account20,
            "value": w3.toWei(valueShare, "ether"),
            "gas": gasUsage,
            "maxFeePerGas": w3.toWei(maxGasShare,"gwei"),
            "maxPriorityFeePerGas": w3.toWei(maxPrioShare,"gwei"),
            "chainId": chainId,
    }
    signed_tx = w3.eth.account.sign_transaction(my_tx, private_keyMain)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = w3.toHex(tx_hash)
    print (f"txhash:{tx_hash}")
    print ("Share ETH to Wallet 20 finished")



## Share Functions Below ##

if ToolFunction == "M1": 
    buy1()

if ToolFunction == "M2":
    buy1()
    buy2()
    
if ToolFunction == "M3":
    buy1()
    buy2()
    buy3()

if ToolFunction == "M4":
    buy1()
    buy2()
    buy3()
    buy4()

if ToolFunction == "M5":
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()

if ToolFunction == "M6":
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()

if ToolFunction == "M7":
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()
    buy7()

if ToolFunction == "M8":
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()
    buy7()
    buy8()

if ToolFunction == "M9":
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()
    buy7()
    buy8()
    buy9()

if ToolFunction == "M10":
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()
    buy7()
    buy8()
    buy9()
    buy10()

if ToolFunction == "M11":
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()
    buy7()
    buy8()
    buy9()
    buy10()
    buy11()

if ToolFunction == "M12":
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()
    buy7()
    buy8()
    buy9()
    buy10()
    buy11()
    buy12()

if ToolFunction == "M13":
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()
    buy7()
    buy8()
    buy9()
    buy10()
    buy11()
    buy12()
    buy13()

if ToolFunction == "M14":
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()
    buy7()
    buy8()
    buy9()
    buy10()
    buy11()
    buy12()
    buy13()
    buy14()

if ToolFunction == "M15":
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()
    buy7()
    buy8()
    buy9()
    buy10()
    buy11()
    buy12()
    buy13()
    buy14()
    buy15()

if ToolFunction == "M16":
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()
    buy7()
    buy8()
    buy9()
    buy10()
    buy11()
    buy12()
    buy13()
    buy14()
    buy15()
    buy16()

if ToolFunction == "M17":
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()
    buy7()
    buy8()
    buy9()
    buy10()
    buy11()
    buy12()
    buy13()
    buy14()
    buy15()
    buy16()
    buy17()

if ToolFunction == "M18": 
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()
    buy7()
    buy8()
    buy9()
    buy10()
    buy11()
    buy12()
    buy13()
    buy14()
    buy15()
    buy16()
    buy17()
    buy18()

if ToolFunction == "M19":
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()
    buy7()
    buy8()
    buy9()
    buy10()
    buy11()
    buy12()
    buy13()
    buy14()
    buy15()
    buy16()
    buy17()
    buy18()
    buy19()

if ToolFunction == "M20": 
    buy1()
    buy2()
    buy3()
    buy4()
    buy5()
    buy6()
    buy7()
    buy8()
    buy9()
    buy10()
    buy11()
    buy12()
    buy13()
    buy14()
    buy15()
    buy16()
    buy17()
    buy18()
    buy19()
    buy20()

## Share Functions Below ##

if ToolFunction == "S1": 
    share1()

if ToolFunction == "S2":
    share1()
    share2()

if ToolFunction == "S3":
    share1()
    share2()
    share3()

if ToolFunction == "S4":
    share1()
    share2()
    share3()
    share4()

if ToolFunction == "S5":
    share1()
    share2()
    share3()
    share4()
    share5()

if ToolFunction == "S6":
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()

if ToolFunction == "S7":
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()

if ToolFunction == "S8":
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()

if ToolFunction == "S9":
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()

if ToolFunction == "S10":
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()

if ToolFunction == "S11":
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()

if ToolFunction == "S12":
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    
if ToolFunction == "S13":
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()

if ToolFunction == "S14":
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    share14()

if ToolFunction == "S15":
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    share14()
    share15()

if ToolFunction == "S16":
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    share14()
    share15()
    share16()

if ToolFunction == "S17":
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    share14()
    share15()
    share16()
    share17()

if ToolFunction == "S18": 
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    share14()
    share15()
    share16()
    share17()
    share18()

if ToolFunction == "S19":
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    share14()
    share15()
    share16()
    share17()
    share18()
    share19()

if ToolFunction == "S20": 
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    share14()
    share15()
    share16()
    share17()
    share18()
    share19()
    share20()

## Share and Mint Functions Below ##

if ToolFunction == "SAM1": 
    Block = w3.eth.get_block_number()
    share1()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()

if ToolFunction == "SAM2": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()

if ToolFunction == "SAM3": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()

if ToolFunction == "SAM4": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()

if ToolFunction == "SAM5": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()

if ToolFunction == "SAM6": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()

if ToolFunction == "SAM7": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()
        buy7()

if ToolFunction == "SAM8": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()
        buy7()
        buy8()

if ToolFunction == "SAM9": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()
        buy7()
        buy8()
        buy9()

if ToolFunction == "SAM10": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()
        buy7()
        buy8()
        buy9()
        buy10()

if ToolFunction == "SAM11": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()
        buy7()
        buy8()
        buy9()
        buy10()
        buy11()

if ToolFunction == "SAM12": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()
        buy7()
        buy8()
        buy9()
        buy10()
        buy11()
        buy12()

if ToolFunction == "SAM13": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()
        buy7()
        buy8()
        buy9()
        buy10()
        buy11()
        buy12()
        buy13()

if ToolFunction == "SAM14": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    share14()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()
        buy7()
        buy8()
        buy9()
        buy10()
        buy11()
        buy12()
        buy13()
        buy14()

if ToolFunction == "SAM15": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    share14()
    share15()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()
        buy7()
        buy8()
        buy9()
        buy10()
        buy11()
        buy12()
        buy13()
        buy14()
        buy15()

if ToolFunction == "SAM16": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    share14()
    share15()
    share16()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()
        buy7()
        buy8()
        buy9()
        buy10()
        buy11()
        buy12()
        buy13()
        buy14()
        buy15()
        buy16()

if ToolFunction == "SAM17": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    share14()
    share15()
    share16()
    share17()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()
        buy7()
        buy8()
        buy9()
        buy10()
        buy11()
        buy12()
        buy13()
        buy14()
        buy15()
        buy16()
        buy17()

if ToolFunction == "SAM18": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    share14()
    share15()
    share16()
    share17()
    share18()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()
        buy7()
        buy8()
        buy9()
        buy10()
        buy11()
        buy12()
        buy13()
        buy14()
        buy15()
        buy16()
        buy17()
        buy18()

if ToolFunction == "SAM19": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    share14()
    share15()
    share16()
    share17()
    share18()
    share19()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()
        buy7()
        buy8()
        buy9()
        buy10()
        buy11()
        buy12()
        buy13()
        buy14()
        buy15()
        buy16()
        buy17()
        buy18()
        buy19()

if ToolFunction == "SAM20": 
    Block = w3.eth.get_block_number()
    share1()
    share2()
    share3()
    share4()
    share5()
    share6()
    share7()
    share8()
    share9()
    share10()
    share11()
    share12()
    share13()
    share14()
    share15()
    share16()
    share17()
    share18()
    share19()
    share20()
    while w3.eth.get_block_number() < Block + waitingBlocks:
        time.sleep(5)
    else: 
        buy1()
        buy2()
        buy3()
        buy4()
        buy5()
        buy6()
        buy7()
        buy8()
        buy9()
        buy10()
        buy11()
        buy12()
        buy13()
        buy14()
        buy15()
        buy16()
        buy17()
        buy18()
        buy19()
        buy20()


