





import java.util.List;
import java.util.ArrayList;

public class Manufacturer  {

    private String location;
    private String brand;





    private Wheel wheel;




    private Engine engine;


    public Manufacturer(
        String location,        String brand    ) {
        this.location = location;
        this.brand = brand;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public Wheel getWheel() {
        return wheel;
    }

    public void setWheel(Wheel wheel) {
        this.wheel = wheel;
    }
    public Engine getEngine() {
        return engine;
    }

    public void setEngine(Engine engine) {
        this.engine = engine;
    }

}