





import java.util.List;
import java.util.ArrayList;

public class Items  {

    private String Quantity;
    private String SKUCode;





    private List<Shopping_Cart> shopping_carts;


    public Items(
        String Quantity,        String SKUCode    ) {
        this.Quantity = Quantity;
        this.SKUCode = SKUCode;
        this.shopping_carts = new ArrayList<>();
    }

    public Items(
        String Quantity,        String SKUCode        ArrayList<Shopping_Cart> shopping_carts    ) {
        this.Quantity = Quantity;
        this.SKUCode = SKUCode;
        this.shopping_carts = shopping_carts;
    }

    public String getQuantity() {
        return Quantity;
    }

    public void setQuantity(String Quantity) {
        this.Quantity = Quantity;
    }
    public String getSkucode() {
        return SKUCode;
    }

    public void setSkucode(String SKUCode) {
        this.SKUCode = SKUCode;
    }

    public List<Shopping_Cart> getShopping_carts() {
        return shopping_carts;
    }

    public void addShopping_cart(Shopping_cart shopping_cart) {
        this.shopping_carts.add(shopping_cart);
    }

}