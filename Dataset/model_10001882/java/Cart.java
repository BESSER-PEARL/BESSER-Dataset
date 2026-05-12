





import java.util.List;
import java.util.ArrayList;

public class Cart  {

    private String quantity;
    private String productid;
    private String date;
    private String cartid;





    private pembeli pembeli;


    public Cart(
        String quantity,        String productid,        String date,        String cartid    ) {
        this.quantity = quantity;
        this.productid = productid;
        this.date = date;
        this.cartid = cartid;
    }


    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }
    public String getProductid() {
        return productid;
    }

    public void setProductid(String productid) {
        this.productid = productid;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getCartid() {
        return cartid;
    }

    public void setCartid(String cartid) {
        this.cartid = cartid;
    }

    public pembeli getPembeli() {
        return pembeli;
    }

    public void setPembeli(pembeli pembeli) {
        this.pembeli = pembeli;
    }

}