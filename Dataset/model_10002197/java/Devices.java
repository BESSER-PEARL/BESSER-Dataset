





import java.util.List;
import java.util.ArrayList;

public class Devices  {

    private String name;
    private int price;





    private Items items;


    public Devices(
        String name,        int price    ) {
        this.name = name;
        this.price = price;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public Items getItems() {
        return items;
    }

    public void setItems(Items items) {
        this.items = items;
    }

}