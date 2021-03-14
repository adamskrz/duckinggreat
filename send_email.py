import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

orders = [
    [1, "Ike.milian-lewis@warwick.ac.uk", 4, 1.09],
    [4, "joe.a.harrison@warwick.ac.uk", 1, 0],
    [6, "siddharth.srivastava@warwick.ac.uk", 2, 0],
    [8, "u2000133@live.warwick.ac.uk", 1, 0],
    [10, "samdagnall2@gmail.com", 2, 1.09],
    [17, "samuel.young@warwick.ac.uk", 1, 0],
    [21, "aaron.parmar18@gmail.com", 1, 0],
    [22, "Luca.Seaford@warwick.ac.uk", 2, 0],
    [26, "Tom.Divers@warwick.ac.uk", 1, 0],
    [27, "f.keating@warwick.ac.uk", 2, 0],
    [28, "matmolni@gmail.com", 1, 0],
    [29, "mia.borgese@warwick.ac.uk", 1, 0],
    [30, "yoel.kastro-morlevi@warwick.ac.uk", 2, 0],
    [31, "Anjalika.Patel@warwick.ac.uk", 1, 0],
    [39, "sammydodger39@gmail.com", 3, 0],
    [42, "alexandra.day02@outlook.com", 2, 0],
    [44, "aryadevchavali1@gmail.com", 2, 0],
    [45, "mary.kassayova@warwick.ac.uk", 1, 0],
    [46, "matthew.wight@warwick.ac.uk", 1, 0],
    [47, "kailobouskila@gmail.com", 1, 0],
    [48, "u2014305@live.warwick.ac.uk", 2, 0],
    [52, "S.Coy@warwick.ac.uk", 2, 0],
    [53, "quack@ameliewd.com", 1, 1.09],
    [55, "u2007041@live.warwick.ac.uk", 2, 0],
    [56, "louisfinch14@gmail.com", 2, 0],
    [57, "lukasrutkauskas16@gmail.com", 1, 0],
    [58, "aaron.parmar18@gmail.com", 1, 0],
    [59, "Fergal.O-Kane@warwick.ac.uk", 5, 0],
    [60, "samirrjsh@gmail.com", 1, 0],
    [62, "Rahul.Vanmali@warwick.ac.uk", 1, 0],
    [65, "fred.westthorp@hotmail.co.uk", 2, 0],
    [66, "leoriviera4@gmail.com", 2, 2.50]
]

s = smtplib.SMTP(host='mail.postale.io', port=587)
s.starttls()
s.login("quack@duckinggreat.com", "4ekaiQHKvuvE")

# orders = [orders[9]]

for order in orders:

    order_number = order[0]
    email = order[1]
    quantity = order[2]
    discount = order[3]

    price_per_duck = (2.50 - discount)
    total_price = price_per_duck * quantity

    message = f"""
Hello!

(TL;DR: If you'd like to pick up your duck on Friday, 12th February, it's important you make a payment and reply to this email.)

THE DUCKS ARE INVADING WARWICK.

No, but seriously, we're happy to let you know they look like ducks, waddle like ducks, quack like ducks and are ready for their new homes!

You can pick up your quacking programming/bath buddies from 1530 on Friday, 12th February at the Piazza on Central Campus, unless otherwise arranged. You'll be able to find Leo easily as he'll be the one guy there standing awkwardly with a big bag full of ducks.

If you plan to pick up then, let us know by replying to this email. Please also make a bank transfer to
Name: Leo Riviera
Account number: 56827981
Sort code: 04-00-04

You'll need to include your order number in the reference. We sadly won't be accepting cash. If you're paying for more than one duck, just stick both order numbers in the reference.

Just as a reminder, you're order number order {order_number}, with {quantity} duck{"s" if quantity > 1 else ""} at £{total_price:.2f}.

If you can't make it, don't worry! Subsequent pick-up dates will be announced next week. If you're not on campus yet, we can always hold your ducks until you arrive.

As always, please let us know if you have any questions, comments or concerns.

Cheers,

Josh and Leo

P.S.: When you do get your duck, send us pics and we'll pop them in the gallery at duckinggreat.com.
    """

    msg = MIMEMultipart()

    # setup the parameters of the message
    msg['From'] = "Josh and Leo <quack@duckinggreat.com>"
    msg['To'] = email
    msg['Subject'] = f"Pick up your duck! (Order #{order_number})"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)

    print(f"Order confirmation email {order_number} sent to {email}.")
