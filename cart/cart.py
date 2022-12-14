
from services.models import Services

class Cart:

    def __init__(self, request):

        self.request= request

        self.session= request.session

        cart=self.session.get('cart')

        if not cart:

            cart=self.session['cart']={}

        self.cart = cart

    def add(self, service, quantity=1):
        service_id= str(service.id)

        if service_id not in self.cart:
            self.cart[service_id]= {'quantity': quantity}
        else:
            self.cart[service_id][quantity]+= quantity
        self.save()

    def remove(self,service):
        service_id = str(service.id)
        if service_id in self.cart:
            del self.cart[service_id]

    def save(self):
        self.session.modified= True

    def __iter__(self):
        service_ids=self.cart.keys()
        services=Services.objects.filter(id__in=service_ids)
        cart=self.cart.copy()

        for service in Services:
            cart[str(service.id)]['service_obj']=service

        for item in cart.values():
            yield item


    def __len__(self):
        return len(self.cart.keys())


    def clear(self):
        del self.session['cart']
        self.save()


    def get_total_price(self):
        service_ids=self.cart.keys()
        services=Services.objects.filter(id__in=service_ids)

        return sum(services.price for service in Services)











