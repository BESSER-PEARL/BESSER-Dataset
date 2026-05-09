





import java.util.List;
import java.util.ArrayList;

public class tda593_billing_Service  {

    private String name;
    private int id;
    private float price;



    public tda593_billing_Service(
        String name,        int id,        float price    ) {
        this.name = name;
        this.id = id;
        this.price = price;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }


}