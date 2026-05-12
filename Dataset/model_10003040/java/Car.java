





import java.util.List;
import java.util.ArrayList;

public class Car  {

    private String name;
    private String manufacturer;
    private int stock;
    private String cost;



    public Car(
        String name,        String manufacturer,        int stock,        String cost    ) {
        this.name = name;
        this.manufacturer = manufacturer;
        this.stock = stock;
        this.cost = cost;
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


}