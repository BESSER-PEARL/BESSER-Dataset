





import java.util.List;
import java.util.ArrayList;

public class Product_Item  {

    private String OutofStock__;
    private String totalcost__;
    private int id;
    private float list__;
    private int quantity;





    private Cart_ShoppingCart cart_shoppingcart;




    private GUI_Screen gui_screen;


    public Product_Item(
        String OutofStock__,        String totalcost__,        int id,        float list__,        int quantity    ) {
        this.OutofStock__ = OutofStock__;
        this.totalcost__ = totalcost__;
        this.id = id;
        this.list__ = list__;
        this.quantity = quantity;
    }


    public String getOutofstock__() {
        return OutofStock__;
    }

    public void setOutofstock__(String OutofStock__) {
        this.OutofStock__ = OutofStock__;
    }
    public String getTotalcost__() {
        return totalcost__;
    }

    public void setTotalcost__(String totalcost__) {
        this.totalcost__ = totalcost__;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public float getList__() {
        return list__;
    }

    public void setList__(float list__) {
        this.list__ = list__;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public Cart_ShoppingCart getCart_shoppingcart() {
        return cart_shoppingcart;
    }

    public void setCart_shoppingcart(Cart_ShoppingCart cart_shoppingcart) {
        this.cart_shoppingcart = cart_shoppingcart;
    }
    public GUI_Screen getGui_screen() {
        return gui_screen;
    }

    public void setGui_screen(GUI_Screen gui_screen) {
        this.gui_screen = gui_screen;
    }

}