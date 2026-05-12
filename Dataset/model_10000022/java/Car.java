





import java.util.List;
import java.util.ArrayList;

public class Car  {

    private String engine;
    private int width;
    private int height;
    private int doors;
    private String model;
    private int length;
    private String wheels;



    public Car(
        String engine,        int width,        int height,        int doors,        String model,        int length,        String wheels    ) {
        this.engine = engine;
        this.width = width;
        this.height = height;
        this.doors = doors;
        this.model = model;
        this.length = length;
        this.wheels = wheels;
    }


    public String getEngine() {
        return engine;
    }

    public void setEngine(String engine) {
        this.engine = engine;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getDoors() {
        return doors;
    }

    public void setDoors(int doors) {
        this.doors = doors;
    }
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getWheels() {
        return wheels;
    }

    public void setWheels(String wheels) {
        this.wheels = wheels;
    }


}