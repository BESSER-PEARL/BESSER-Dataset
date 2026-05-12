





import java.util.List;
import java.util.ArrayList;

public class RepairPart  {

    private int stock;
    private String name;
    private String cost;



    public RepairPart(
        int stock,        String name,        String cost    ) {
        this.stock = stock;
        this.name = name;
        this.cost = cost;
    }


    public int getStock() {
        return stock;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }


}