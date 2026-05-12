





import java.util.List;
import java.util.ArrayList;

public class Furniture  {

    private int price;
    private String name;





    private Items items;


    public Furniture(
        int price,        String name    ) {
        this.price = price;
        this.name = name;
    }


    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Items getItems() {
        return items;
    }

    public void setItems(Items items) {
        this.items = items;
    }

}