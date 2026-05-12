





import java.util.List;
import java.util.ArrayList;

public class Cart  {

    private String cartid;
    private String quantity;
    private String date;
    private String productid;





    private pembeli pembeli;


    public Cart(
        String cartid,        String quantity,        String date,        String productid    ) {
        this.cartid = cartid;
        this.quantity = quantity;
        this.date = date;
        this.productid = productid;
    }


    public String getCartid() {
        return cartid;
    }

    public void setCartid(String cartid) {
        this.cartid = cartid;
    }
    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getProductid() {
        return productid;
    }

    public void setProductid(String productid) {
        this.productid = productid;
    }

    public pembeli getPembeli() {
        return pembeli;
    }

    public void setPembeli(pembeli pembeli) {
        this.pembeli = pembeli;
    }

}