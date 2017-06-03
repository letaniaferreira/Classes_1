"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """Both domestic and international melon orders"""

    def __init__(self, species, qty, order_type, tax):
        """All melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax 

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        international_fee = 0
        

        if self.species == "Christmas_Melon":
            base_price = base_price * 1.5
        
        if self.order_type == "international" and self.qty < 10:
            international_fee = 3

        total = ((1 + self.tax) * self.qty * base_price) + international_fee

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self,species,qty):
        """Initialize melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)

        self.country_code = country_code
    
    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """Government Melon Order"""

    def __init__(self, species, qty, passed_inpection):
        """Initialize melon order attributes"""
        super(GovernmentMelonOrder, self). __init__(species, qty, "domestic", 0)

        self.passed_inpection = False

    def mark_inspection(passed):
        """Updates whether melon has passed inspection"""
        
        return self.passed_inpection

#     def get_total(self):
#         """Calculate price, excluding tax."""

#         base_price = 5 * 1.5
#         if qty >= 10:
#             total = (1 + self.tax) * self.qty * base_price
#             if order_type == "international" and qty < 10:
#                 total = ((1 + self.tax) * self.qty * base_price) + 3
#             else:
#                 total = (1 + self.tax) * self.qty * base_price

#         return total
