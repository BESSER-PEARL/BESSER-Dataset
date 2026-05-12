





import java.util.List;
import java.util.ArrayList;

public class product  {

    private String imagefilename;
    private int price;
    private int productid;
    private String productname;





    private cartitem cartitem;


    public product(
        String imagefilename,        int price,        int productid,        String productname    ) {
        this.imagefilename = imagefilename;
        this.price = price;
        this.productid = productid;
        this.productname = productname;
    }


    public String getImagefilename() {
        return imagefilename;
    }

    public void setImagefilename(String imagefilename) {
        this.imagefilename = imagefilename;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public int getProductid() {
        return productid;
    }

    public void setProductid(int productid) {
        this.productid = productid;
    }
    public String getProductname() {
        return productname;
    }

    public void setProductname(String productname) {
        this.productname = productname;
    }

    public cartitem getCartitem() {
        return cartitem;
    }

    public void setCartitem(cartitem cartitem) {
        this.cartitem = cartitem;
    }

}