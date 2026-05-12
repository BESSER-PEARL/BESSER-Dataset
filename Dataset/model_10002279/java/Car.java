





import java.util.List;
import java.util.ArrayList;

public class Car  {

    private int stock;
    private String manufacturer;
    private String cost;
    private String name;



    public Car(
        int stock,        String manufacturer,        String cost,        String name    ) {
        this.stock = stock;
        this.manufacturer = manufacturer;
        this.cost = cost;
        this.name = name;
    }


    public int getStock() {
        return stock;
    }

    public void setStock(int stock) {
        this.stock = stock;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}