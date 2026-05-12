





import java.util.List;
import java.util.ArrayList;

public class Car1  {

    private int doors;
    private int length;
    private String wheels;
    private String model;
    private int height;
    private String engine;
    private int width;



    public Car1(
        int doors,        int length,        String wheels,        String model,        int height,        String engine,        int width    ) {
        this.doors = doors;
        this.length = length;
        this.wheels = wheels;
        this.model = model;
        this.height = height;
        this.engine = engine;
        this.width = width;
    }


    public int getDoors() {
        return doors;
    }

    public void setDoors(int doors) {
        this.doors = doors;
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
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
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


}