





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Basket  {

    private boolean IsEmpty;
    private None Contents;
    private String attribute;





    private Online_Shopping_Checkout online_shopping_checkout;




    private Online_Shopping_Item online_shopping_item;


    public Online_Shopping_Basket(
        boolean IsEmpty,        None Contents,        String attribute    ) {
        this.IsEmpty = IsEmpty;
        this.Contents = Contents;
        this.attribute = attribute;
    }


    public boolean getIsempty() {
        return IsEmpty;
    }

    public void setIsempty(boolean IsEmpty) {
        this.IsEmpty = IsEmpty;
    }
    public None getContents() {
        return Contents;
    }

    public void setContents(None Contents) {
        this.Contents = Contents;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public Online_Shopping_Checkout getOnline_shopping_checkout() {
        return online_shopping_checkout;
    }

    public void setOnline_shopping_checkout(Online_Shopping_Checkout online_shopping_checkout) {
        this.online_shopping_checkout = online_shopping_checkout;
    }
    public Online_Shopping_Item getOnline_shopping_item() {
        return online_shopping_item;
    }

    public void setOnline_shopping_item(Online_Shopping_Item online_shopping_item) {
        this.online_shopping_item = online_shopping_item;
    }

}