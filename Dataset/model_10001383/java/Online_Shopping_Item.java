





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Item  {

    private String ProductID;
    private String Description;
    private String Name;
    private int Price;



    public Online_Shopping_Item(
        String ProductID,        String Description,        String Name,        int Price    ) {
        this.ProductID = ProductID;
        this.Description = Description;
        this.Name = Name;
        this.Price = Price;
    }


    public String getProductid() {
        return ProductID;
    }

    public void setProductid(String ProductID) {
        this.ProductID = ProductID;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getPrice() {
        return Price;
    }

    public void setPrice(int Price) {
        this.Price = Price;
    }


}