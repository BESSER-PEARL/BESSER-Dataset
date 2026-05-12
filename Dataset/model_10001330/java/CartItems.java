





import java.util.List;
import java.util.ArrayList;

public class CartItems  {

    private String Price;
    private String Name;



    public CartItems(
        String Price,        String Name    ) {
        this.Price = Price;
        this.Name = Name;
    }


    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}