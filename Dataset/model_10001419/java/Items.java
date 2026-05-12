





import java.util.List;
import java.util.ArrayList;

public class Items  {

    private String Description;





    private Shopping_Cart shopping_cart;


    public Items(
        String Description    ) {
        this.Description = Description;
    }


    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }

    public Shopping_Cart getShopping_cart() {
        return shopping_cart;
    }

    public void setShopping_cart(Shopping_Cart shopping_cart) {
        this.shopping_cart = shopping_cart;
    }

}