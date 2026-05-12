





import java.util.List;
import java.util.ArrayList;

public class Car  {

    private String cost;
    private String manufacturer;
    private String name;
    private int stock;



    public Car(
        String cost,        String manufacturer,        String name,        int stock    ) {
        this.cost = cost;
        this.manufacturer = manufacturer;
        this.name = name;
        this.stock = stock;
    }


    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }
    public String getManufacturer() {
        return manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getStock() {
        return stock;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }


}