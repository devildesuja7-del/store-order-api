from pydantic import BaseModel, Field

class OrderItem(BaseModel):
    product: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    
    @property
    def total(self):
        return self.quantity*self.unit_price