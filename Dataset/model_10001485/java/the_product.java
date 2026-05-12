





import java.util.List;
import java.util.ArrayList;

public class the_product  {

    private String name;
    private String type;
    private int price;



    public the_product(
        String name,        String type,        int price    ) {
        this.name = name;
        this.type = type;
        this.price = price;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }


}