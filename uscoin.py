import json


class USCoin:
    def __init__(self):
        self.denomination = ""
        self.year = 0
        self.condition = ""
        self.value = 0.0

    def to_json(self):
        return {
            "denomination": self.denomination,
            "year": self.year,
            "condition": self.condition,
            "value": self.value
        }

    # Setters
    def set_denomination(self, denomination):
        self.denomination = denomination

    def set_year(self, year):
        self.year = year

    def set_condition(self, condition):
        self.condition = condition

    def set_value(self, value):
        self.value = value

    # Getters
    def get_denomination(self):
        return self.denomination

    def get_year(self):
        return self.year

    def get_condition(self):
        return self.condition

    def get_value(self):
        return self.value

class CoinCollection:
    def __init__(self):
        self.coins = []

    def insert_coin(self, coin_data):
        try:
            with open('coin_collection.json', 'r') as file:
                coins = json.load(file)
        except json.JSONDecodeError:
            coins = []
        # Append new coin data
        coins.append(coin_data)

        # Write updated data back to JSON file
        with open('coin_collection.json', 'w') as file:
            json.dump(coins, file, indent=4)

    def filter_coins(self, filter_value):
        # Try to read existing data from JSON file
        with open('coin_collection.json', 'r') as file:
            coins = json.load(file)
        # Filter coins based on denomination
        filtered_coins = [coin for coin in coins if coin['denomination'] == filter_value]
        return filtered_coins

    def sort_coins_by_value(self):
        # Try to read existing data from JSON file
        with open('coin_collection.json', 'r') as file:
            coins = json.load(file)
        # Sort coins by value
        sorted_coins = sorted(coins, key=lambda coin: coin['value'])
        return sorted_coins

    def remove_coin(self, denomination):
        with open('coin_collection.json', 'r') as file:
            coins = json.load(file)
        filtered_coins = [coin for coin in coins if coin['denomination'] != denomination]
        with open('coin_collection.json', 'w') as file:
            json.dump(filtered_coins, file, indent=4)
