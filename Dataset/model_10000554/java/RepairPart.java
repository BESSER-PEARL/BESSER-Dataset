





import java.util.List;
import java.util.ArrayList;

public class RepairPart  {

    private String name;
    private String cost;
    private int stock;



    public RepairPart(
        String name,        String cost,        int stock    ) {
        this.name = name;
        this.cost = cost;
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
    public int getStock() {
        return stock;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }


}