





import java.util.List;
import java.util.ArrayList;

public class Car  {

    private String cost;
    private String name;
    private int stock;
    private String manufacturer;



    public Car(
        String cost,        String name,        int stock,        String manufacturer    ) {
        this.cost = cost;
        this.name = name;
        this.stock = stock;
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


}