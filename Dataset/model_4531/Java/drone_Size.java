





import java.util.List;
import java.util.ArrayList;

public class drone_Size  {

    private float height;
    private float propellerSize;
    private float length;
    private float width;
    private int propellers;
    private float weight;





    private drone_Drone drone_drone;


    public drone_Size(
        float height,        float propellerSize,        float length,        float width,        int propellers,        float weight    ) {
        this.height = height;
        this.propellerSize = propellerSize;
        this.length = length;
        this.width = width;
        this.propellers = propellers;
        this.weight = weight;
    }


    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public float getPropellersize() {
        return propellerSize;
    }

    public void setPropellersize(float propellerSize) {
        this.propellerSize = propellerSize;
    }
    public float getLength() {
        return length;
    }

    public void setLength(float length) {
        this.length = length;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public int getPropellers() {
        return propellers;
    }

    public void setPropellers(int propellers) {
        this.propellers = propellers;
    }
    public float getWeight() {
        return weight;
    }

    public void setWeight(float weight) {
        this.weight = weight;
    }

    public drone_Drone getDrone_drone() {
        return drone_drone;
    }

    public void setDrone_drone(drone_Drone drone_drone) {
        this.drone_drone = drone_drone;
    }

}