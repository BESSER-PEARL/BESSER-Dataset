





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private int Quantity;
    private String Name;
    private String attribute;



    public Item(
        int Quantity,        String Name,        String attribute    ) {
        this.Quantity = Quantity;
        this.Name = Name;
        this.attribute = attribute;
    }


    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}