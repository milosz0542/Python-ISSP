class Items:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item["price"] for item in self.items)

class sendEmail:
    def __init__(self, customer_email, total):
        self.customer_email = customer_email
        self.total = total

    def send_email_notification(self):
        message = f"Your order total is {self.total}.\n Thank you for shopping"
        print(f"Sending email to: {self.customer_email}:\n {message}")


# init items
order1 = Items([{"name": "Book", "price": 10}, {"name": "Pencil", "price": 2}])
print(order1.calculate_total())

customer_email = "123456@uwr.edu.pl"
email = sendEmail(customer_email, order1.calculate_total())
email.send_email_notification()