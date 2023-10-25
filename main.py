class SecurityLending:
    def __init__(self, stock_symbol, quantity, lending_fee, borrower,inventory):
        self.stock_symbol = stock_symbol
        self.quantity = quantity
        self.lending_fee = lending_fee
        self.borrower = borrower
        self.inventory = inventory

    def initiate_lending(self):
        if self.is_stock_available():
            # Reserve the stock for the borrower
            self.reserve_stock_for_borrower()
            # Calculate the lending amount and generate a contract
            lending_amount = self.calculate_lending_amount()
            contract = self.generate_lending_contract(lending_amount)
            # Send the contract to the borrower
            self.send_contract_to_borrower(contract)
            return contract
        else:
            raise Exception("Stock not available for lending")

    def is_stock_available(self):
        if self.inventory > self.quantity:
            pass
        else:
            raise Exception("Stock not available for lending")

    def reserve_stock_for_borrower(self):
        # Inventory reduced by borrower reserve quantity
        if self.inventory > self.quantity:
            self.inventory = self.inventory - self.quantity
        else:
            self.inventory  # Replace with actual implementation

    def calculate_lending_amount(self):
        #lending amount based on the quantity and lending fee
        return self.quantity * self.lending_fee

    def generate_lending_contract(self, lending_amount):
        # Generating contract containing lending details
        contract = {
            "stock_symbol": self.stock_symbol,
            "quantity": self.quantity,
            "lending_fee": self.lending_fee,
            "borrower": self.borrower,
            "lending_amount": lending_amount,
        }
        return contract

    def send_contract_to_borrower(self, contract):
        # Add logic to send the contract to the borrower
        print("Contract sent to the borrower:", contract)