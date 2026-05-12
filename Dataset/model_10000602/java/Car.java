





import java.util.List;
import java.util.ArrayList;

public class Car  {

    private String name;
    private String manufacturer;
    private String cost;
    private int stock;



    public Car(
        String name,        String manufacturer,        String cost,        int stock    ) {
        this.name = name;
        this.manufacturer = manufacturer;
        this.cost = cost;
        this.stock = stock;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getManufacturer() {
        return manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
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