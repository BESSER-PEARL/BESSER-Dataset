





import java.util.List;
import java.util.ArrayList;

public class Vehicle  {

    private String price;
    private String brand;
    private String engine;



    public Vehicle(
        String price,        String brand,        String engine    ) {
        this.price = price;
        this.brand = brand;
        this.engine = engine;
    }


    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }
    public String getEngine() {
        return engine;
    }

    public void setEngine(String engine) {
        this.engine = engine;
    }


}