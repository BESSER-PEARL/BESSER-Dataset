





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_BasketItem  {

    private int Quantity;
    private String ProductID;





    private Online_Shopping_Basket online_shopping_basket;


    public Online_Shopping_BasketItem(
        int Quantity,        String ProductID    ) {
        this.Quantity = Quantity;
        this.ProductID = ProductID;
    }


    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public String getProductid() {
        return ProductID;
    }

    public void setProductid(String ProductID) {
        this.ProductID = ProductID;
    }

    public Online_Shopping_Basket getOnline_shopping_basket() {
        return online_shopping_basket;
    }

    public void setOnline_shopping_basket(Online_Shopping_Basket online_shopping_basket) {
        this.online_shopping_basket = online_shopping_basket;
    }

}