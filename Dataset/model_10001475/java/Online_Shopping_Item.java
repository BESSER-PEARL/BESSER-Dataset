





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Item  {

    private int Price;
    private String Name;
    private String Description;
    private String Product_ID;



    public Online_Shopping_Item(
        int Price,        String Name,        String Description,        String Product_ID    ) {
        this.Price = Price;
        this.Name = Name;
        this.Description = Description;
        this.Product_ID = Product_ID;
    }


    public int getPrice() {
        return Price;
    }

    public void setPrice(int Price) {
        this.Price = Price;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getProduct_id() {
        return Product_ID;
    }

    public void setProduct_id(String Product_ID) {
        this.Product_ID = Product_ID;
    }


}