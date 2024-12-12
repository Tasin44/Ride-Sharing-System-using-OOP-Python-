class Payment():
    @staticmethod
    def process_payment(payment_method,amount):
        print(f'Processing payment of {amount} using {payment_method}.')