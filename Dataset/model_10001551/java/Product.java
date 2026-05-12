





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String Product_Name;
    private int id;
    private int Price;





    private Suppliers suppliers;




    private Shopping_cart shopping_cart;


    public Product(
        String Product_Name,        int id,        int Price    ) {
        this.Product_Name = Product_Name;
        this.id = id;
        this.Price = Price;
    }


    public String getProduct_name() {
        return Product_Name;
    }

    public void setProduct_name(String Product_Name) {
        this.Product_Name = Product_Name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getPrice() {
        return Price;
    }

    public void setPrice(int Price) {
        this.Price = Price;
    }

    public Suppliers getSuppliers() {
        return suppliers;
    }

    public void setSuppliers(Suppliers suppliers) {
        this.suppliers = suppliers;
    }
    public Shopping_cart getShopping_cart() {
        return shopping_cart;
    }

    public void setShopping_cart(Shopping_cart shopping_cart) {
        this.shopping_cart = shopping_cart;
    }

}