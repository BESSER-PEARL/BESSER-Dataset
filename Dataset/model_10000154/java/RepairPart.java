





import java.util.List;
import java.util.ArrayList;

public class RepairPart  {

    private int stock;
    private String cost;
    private String name;



    public RepairPart(
        int stock,        String cost,        String name    ) {
        this.stock = stock;
        this.cost = cost;
        this.name = name;
    }


    public int getStock() {
        return stock;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }
    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}