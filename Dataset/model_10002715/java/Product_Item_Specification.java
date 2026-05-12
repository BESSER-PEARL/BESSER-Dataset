





import java.util.List;
import java.util.ArrayList;

public class Product_Item_Specification  {

    private int quantity;
    private float price;
    private String ItemSpecs__;
    private int id;
    private String Brand__;





    private Product_Item product_item;


    public Product_Item_Specification(
        int quantity,        float price,        String ItemSpecs__,        int id,        String Brand__    ) {
        this.quantity = quantity;
        this.price = price;
        this.ItemSpecs__ = ItemSpecs__;
        this.id = id;
        this.Brand__ = Brand__;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getItemspecs__() {
        return ItemSpecs__;
    }

    public void setItemspecs__(String ItemSpecs__) {
        this.ItemSpecs__ = ItemSpecs__;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getBrand__() {
        return Brand__;
    }

    public void setBrand__(String Brand__) {
        this.Brand__ = Brand__;
    }

    public Product_Item getProduct_item() {
        return product_item;
    }

    public void setProduct_item(Product_Item product_item) {
        this.product_item = product_item;
    }

}