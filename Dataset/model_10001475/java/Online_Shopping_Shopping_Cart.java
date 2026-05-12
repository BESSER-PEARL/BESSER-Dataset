





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Shopping_Cart  {

    private boolean Is_Empty;
    private None Contents;





    private Online_Shopping_Item online_shopping_item;




    private Online_Shopping_Checkout online_shopping_checkout;


    public Online_Shopping_Shopping_Cart(
        boolean Is_Empty,        None Contents    ) {
        this.Is_Empty = Is_Empty;
        this.Contents = Contents;
    }


    public boolean getIs_empty() {
        return Is_Empty;
    }

    public void setIs_empty(boolean Is_Empty) {
        this.Is_Empty = Is_Empty;
    }
    public None getContents() {
        return Contents;
    }

    public void setContents(None Contents) {
        this.Contents = Contents;
    }

    public Online_Shopping_Item getOnline_shopping_item() {
        return online_shopping_item;
    }

    public void setOnline_shopping_item(Online_Shopping_Item online_shopping_item) {
        this.online_shopping_item = online_shopping_item;
    }
    public Online_Shopping_Checkout getOnline_shopping_checkout() {
        return online_shopping_checkout;
    }

    public void setOnline_shopping_checkout(Online_Shopping_Checkout online_shopping_checkout) {
        this.online_shopping_checkout = online_shopping_checkout;
    }

}