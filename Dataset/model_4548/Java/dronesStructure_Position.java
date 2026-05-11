





import java.util.List;
import java.util.ArrayList;

public class dronesStructure_Position  {

    private float y;
    private float z;
    private float x;





    private dronesStructure_Drone dronesstructure_drone;


    public dronesStructure_Position(
        float y,        float z,        float x    ) {
        this.y = y;
        this.z = z;
        this.x = x;
    }


    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public float getZ() {
        return z;
    }

    public void setZ(float z) {
        this.z = z;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }

    public dronesStructure_Drone getDronesstructure_drone() {
        return dronesstructure_drone;
    }

    public void setDronesstructure_drone(dronesStructure_Drone dronesstructure_drone) {
        this.dronesstructure_drone = dronesstructure_drone;
    }

}