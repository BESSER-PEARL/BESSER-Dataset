





import java.util.List;
import java.util.ArrayList;

public class Models_Product  {

    private String imagefilename;
    private int productid;
    private int quantity;
    private String productname;
    private float price;





    private Models_LineItem models_lineitem;




    private dao_ProductDao_Interface dao_productdao_interface;


    public Models_Product(
        String imagefilename,        int productid,        int quantity,        String productname,        float price    ) {
        this.imagefilename = imagefilename;
        this.productid = productid;
        this.quantity = quantity;
        this.productname = productname;
        this.price = price;
    }


    public String getImagefilename() {
        return imagefilename;
    }

    public void setImagefilename(String imagefilename) {
        this.imagefilename = imagefilename;
    }
    public int getProductid() {
        return productid;
    }

    public void setProductid(int productid) {
        this.productid = productid;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getProductname() {
        return productname;
    }

    public void setProductname(String productname) {
        this.productname = productname;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public Models_LineItem getModels_lineitem() {
        return models_lineitem;
    }

    public void setModels_lineitem(Models_LineItem models_lineitem) {
        this.models_lineitem = models_lineitem;
    }
    public dao_ProductDao_Interface getDao_productdao_interface() {
        return dao_productdao_interface;
    }

    public void setDao_productdao_interface(dao_ProductDao_Interface dao_productdao_interface) {
        this.dao_productdao_interface = dao_productdao_interface;
    }

}