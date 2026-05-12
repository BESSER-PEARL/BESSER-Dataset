





import java.util.List;
import java.util.ArrayList;

public class Shopping_cart  {

    private int date;
    private None change_to_cart__;
    private int productId;
    private int quantity;
    private None Checkout__;
    private int cartId;
    private None Add_items_to_shopping_cart__;
    private None Delete_from_Shopping_Cart__;





    private Customer customer;


    public Shopping_cart(
        int date,        None change_to_cart__,        int productId,        int quantity,        None Checkout__,        int cartId,        None Add_items_to_shopping_cart__,        None Delete_from_Shopping_Cart__    ) {
        this.date = date;
        this.change_to_cart__ = change_to_cart__;
        this.productId = productId;
        this.quantity = quantity;
        this.Checkout__ = Checkout__;
        this.cartId = cartId;
        this.Add_items_to_shopping_cart__ = Add_items_to_shopping_cart__;
        this.Delete_from_Shopping_Cart__ = Delete_from_Shopping_Cart__;
    }


    public int getDate() {
        return date;
    }

    public void setDate(int date) {
        this.date = date;
    }
    public None getChange_to_cart__() {
        return change_to_cart__;
    }

    public void setChange_to_cart__(None change_to_cart__) {
        this.change_to_cart__ = change_to_cart__;
    }
    public int getProductid() {
        return productId;
    }

    public void setProductid(int productId) {
        this.productId = productId;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public None getCheckout__() {
        return Checkout__;
    }

    public void setCheckout__(None Checkout__) {
        this.Checkout__ = Checkout__;
    }
    public int getCartid() {
        return cartId;
    }

    public void setCartid(int cartId) {
        this.cartId = cartId;
    }
    public None getAdd_items_to_shopping_cart__() {
        return Add_items_to_shopping_cart__;
    }

    public void setAdd_items_to_shopping_cart__(None Add_items_to_shopping_cart__) {
        this.Add_items_to_shopping_cart__ = Add_items_to_shopping_cart__;
    }
    public None getDelete_from_shopping_cart__() {
        return Delete_from_Shopping_Cart__;
    }

    public void setDelete_from_shopping_cart__(None Delete_from_Shopping_Cart__) {
        this.Delete_from_Shopping_Cart__ = Delete_from_Shopping_Cart__;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}