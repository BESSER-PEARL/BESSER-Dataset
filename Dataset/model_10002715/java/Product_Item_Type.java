





import java.util.List;
import java.util.ArrayList;

public class Product_Item_Type  {

    private int quantity;
    private String ItemType__;
    private String Avail__;
    private float price;
    private int id;





    private Product_Item product_item;


    public Product_Item_Type(
        int quantity,        String ItemType__,        String Avail__,        float price,        int id    ) {
        this.quantity = quantity;
        this.ItemType__ = ItemType__;
        this.Avail__ = Avail__;
        this.price = price;
        this.id = id;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getItemtype__() {
        return ItemType__;
    }

    public void setItemtype__(String ItemType__) {
        this.ItemType__ = ItemType__;
    }
    public String getAvail__() {
        return Avail__;
    }

    public void setAvail__(String Avail__) {
        this.Avail__ = Avail__;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Product_Item getProduct_item() {
        return product_item;
    }

    public void setProduct_item(Product_Item product_item) {
        this.product_item = product_item;
    }

}