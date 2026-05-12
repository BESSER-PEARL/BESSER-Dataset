





import java.util.List;
import java.util.ArrayList;

public class M6  {

    private None engine;
    private String color;
    private String manufacturer;



    public M6(
        None engine,        String color,        String manufacturer    ) {
        this.engine = engine;
        this.color = color;
        this.manufacturer = manufacturer;
    }


    public None getEngine() {
        return engine;
    }

    public void setEngine(None engine) {
        this.engine = engine;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getManufacturer() {
        return manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }


}