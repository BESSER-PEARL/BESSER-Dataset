





import java.util.List;
import java.util.ArrayList;

public class DetailCart  {

    private String DetailCartInfo;
    private int ProductID;
    private int DetailCartID;
    private int CartID;





    private Cart cart;




    private List<Products> productss;


    public DetailCart(
        String DetailCartInfo,        int ProductID,        int DetailCartID,        int CartID    ) {
        this.DetailCartInfo = DetailCartInfo;
        this.ProductID = ProductID;
        this.DetailCartID = DetailCartID;
        this.CartID = CartID;
        this.productss = new ArrayList<>();
    }

    public DetailCart(
        String DetailCartInfo,        int ProductID,        int DetailCartID,        int CartID        ArrayList<Products> productss    ) {
        this.DetailCartInfo = DetailCartInfo;
        this.ProductID = ProductID;
        this.DetailCartID = DetailCartID;
        this.CartID = CartID;
        this.productss = productss;
    }

    public String getDetailcartinfo() {
        return DetailCartInfo;
    }

    public void setDetailcartinfo(String DetailCartInfo) {
        this.DetailCartInfo = DetailCartInfo;
    }
    public int getProductid() {
        return ProductID;
    }

    public void setProductid(int ProductID) {
        this.ProductID = ProductID;
    }
    public int getDetailcartid() {
        return DetailCartID;
    }

    public void setDetailcartid(int DetailCartID) {
        this.DetailCartID = DetailCartID;
    }
    public int getCartid() {
        return CartID;
    }

    public void setCartid(int CartID) {
        this.CartID = CartID;
    }

    public Cart getCart() {
        return cart;
    }

    public void setCart(Cart cart) {
        this.cart = cart;
    }
    public List<Products> getProductss() {
        return productss;
    }

    public void addProducts(Products products) {
        this.productss.add(products);
    }

}