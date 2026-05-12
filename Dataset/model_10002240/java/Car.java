





import java.util.List;
import java.util.ArrayList;

public class Car  {

    private int height;
    private int length;
    private String wheels;
    private String model;
    private int width;
    private String engine;
    private int doors;



    public Car(
        int height,        int length,        String wheels,        String model,        int width,        String engine,        int doors    ) {
        this.height = height;
        this.length = length;
        this.wheels = wheels;
        this.model = model;
        this.width = width;
        this.engine = engine;
        this.doors = doors;
    }


    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
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
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getEngine() {
        return engine;
    }

    public void setEngine(String engine) {
        this.engine = engine;
    }
    public int getDoors() {
        return doors;
    }

    public void setDoors(int doors) {
        this.doors = doors;
    }


}