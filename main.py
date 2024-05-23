import json
from uscoin import USCoin, CoinCollection

class CoinUi():
    def __init__(self):
        self.coins = []
        self.us_coin = USCoin()
        self.coin_collection = CoinCollection()


    def start(self):
        while True:
            print("Please select an option 1: Add Coin, 2: Remove Coin, 3: Search, 4: Sort, 5: Exit")
            choice = int(input())
            if choice == 1:
                self.add_coin()
            elif choice == 2:
                self.remove_coin()
            elif choice == 3:
                self.search_coin()
            elif choice == 4:
                self.sort_coin()
            elif choice == 5:
                print("Exiting..")
                break

    def add_coin(self):
        denomination = input("Enter Denomination: ")
        year = int(input("Enter Year: "))
        condition = input("Enter Condition: ")
        value = float(input("Enter Value: "))
        self.us_coin.set_denomination(denomination)
        self.us_coin.set_year(year)
        self.us_coin.set_condition(condition)
        self.us_coin.set_value(value)
        self.coin_collection.insert_coin(self.us_coin.to_json())

    def remove_coin(self):
        denomination = input("Enter Coin Denomination to Remove: ")
        self.coin_collection.remove_coin(denomination)

    def search_coin(self):
        denomination = input("Enter Coin Denomination to Search: ")
        coins = self.coin_collection.filter_coins(denomination)
        for coin in coins:
            print(json.dumps(coin, indent=4))

    def sort_coin(self):
      sorted_coins = self.coin_collection.sort_coins_by_value()
      for coin in sorted_coins:
          print(json.dumps(coin, indent=4))


if __name__ == "__main__":
    ui = CoinUi()
    ui.start()
