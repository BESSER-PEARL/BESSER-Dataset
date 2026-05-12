





import java.util.List;
import java.util.ArrayList;

public class ShoppingCartExample_Order  {

    private int id;





    private ShoppingCartExample_ShoppingCart shoppingcartexample_shoppingcart;




    private List<ShoppingCartExample_LineItem> shoppingcartexample_lineitems;


    public ShoppingCartExample_Order(
        int id    ) {
        this.id = id;
        this.shoppingcartexample_lineitems = new ArrayList<>();
    }

    public ShoppingCartExample_Order(
        int id        ArrayList<ShoppingCartExample_LineItem> shoppingcartexample_lineitems    ) {
        this.id = id;
        this.shoppingcartexample_lineitems = shoppingcartexample_lineitems;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public ShoppingCartExample_ShoppingCart getShoppingcartexample_shoppingcart() {
        return shoppingcartexample_shoppingcart;
    }

    public void setShoppingcartexample_shoppingcart(ShoppingCartExample_ShoppingCart shoppingcartexample_shoppingcart) {
        this.shoppingcartexample_shoppingcart = shoppingcartexample_shoppingcart;
    }
    public List<ShoppingCartExample_LineItem> getShoppingcartexample_lineitems() {
        return shoppingcartexample_lineitems;
    }

    public void addShoppingcartexample_lineitem(Shoppingcartexample_lineitem shoppingcartexample_lineitem) {
        this.shoppingcartexample_lineitems.add(shoppingcartexample_lineitem);
    }

}