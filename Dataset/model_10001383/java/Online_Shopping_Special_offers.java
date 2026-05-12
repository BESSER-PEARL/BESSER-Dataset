





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Special_offers  {

    private int Discount;
    private String Price;





    private Online_Shopping_BasketItem online_shopping_basketitem;


    public Online_Shopping_Special_offers(
        int Discount,        String Price    ) {
        this.Discount = Discount;
        this.Price = Price;
    }


    public int getDiscount() {
        return Discount;
    }

    public void setDiscount(int Discount) {
        this.Discount = Discount;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }

    public Online_Shopping_BasketItem getOnline_shopping_basketitem() {
        return online_shopping_basketitem;
    }

    public void setOnline_shopping_basketitem(Online_Shopping_BasketItem online_shopping_basketitem) {
        this.online_shopping_basketitem = online_shopping_basketitem;
    }

}