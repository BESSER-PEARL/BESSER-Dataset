





import java.util.List;
import java.util.ArrayList;

public class Car  {

    private int stock;
    private String manufacturer;
    private String name;
    private String cost;



    public Car(
        int stock,        String manufacturer,        String name,        String cost    ) {
        this.stock = stock;
        this.manufacturer = manufacturer;
        this.name = name;
        this.cost = cost;
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