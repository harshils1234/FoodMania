from django.db import models
from foodmania.models import TimeStampedModel, Food
from user.models import User, UserAddress


class Cart(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mycart')
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"Cart: {self.id} User: {self.user}"

    @property
    def cart_total(self):
        total = 0
        for item in self.carts.all():
            total += item.sub_total()
        return total

    @property
    def total_items(self):
        return self.carts.count()

    @property
    def total_tax(self):
        return round(self.cart_total * (18 / 100), 2)

    @property
    def delivery_charges(self):
        if self.cart_total >= 500:
            return 0
        return 50

    @property
    def order_total(self):
        return self.cart_total + self.total_tax + self.delivery_charges


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, related_name='carts')
    item = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='selected_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"ID: {self.id}, Cart_ID: {self.cart}, Food_item: {self.item}, Quantity: {self.quantity}"

    def sub_total(self):
        return self.quantity * self.item.price

    def item_quantity(self):
        return self.quantity


class Order(TimeStampedModel):
    STATUS = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Delivered', 'Delivered'),
        ('Deleted', 'Deleted'),
        ('Cancelled', 'Cancelled')
    )

    order = models.CharField(max_length=10, null=True, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, related_name='cart')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myorders')
    total_amount = models.FloatField(default=0)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    delivery_address = models.ForeignKey(UserAddress, on_delete=models.SET_NULL, null=True,
                                         related_name='myaddress')

    class Meta:
        ordering = ['id']

    def save(self, **kwargs):
        self.total_amount = self.cart.order_total
        return super(Order, self).save(**kwargs)

    def __str__(self):
        return str(self.order)


class OrderPayment(TimeStampedModel):
    PAYMENT_STATUS = (
        ('Success', 'Success'),
        ('Failure', 'Failure'),
        ('Pending', 'Pending')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mypayments',
                             null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payment',
                              null=True, blank=True)
    status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='Pending',
                              null=True, blank=True)
    provider_order_id = models.CharField(max_length=40, null=False, blank=False)
    payment_id = models.CharField(max_length=40, null=False, blank=False)
    signature_id = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return str(self.order)


class Reservation(TimeStampedModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    date = models.DateField()
    time = models.CharField(max_length=20)
    people = models.PositiveSmallIntegerField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class ContactUs(TimeStampedModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    subject = models.CharField(max_length=70)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class NewsLetter(TimeStampedModel):
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return self.email
