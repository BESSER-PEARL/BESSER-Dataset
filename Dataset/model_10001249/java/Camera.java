





import java.util.List;
import java.util.ArrayList;

public class Camera  {

    private int CameraID;





    private Door_Sensor door_sensor;


    public Camera(
        int CameraID    ) {
        this.CameraID = CameraID;
    }


    public int getCameraid() {
        return CameraID;
    }

    public void setCameraid(int CameraID) {
        this.CameraID = CameraID;
    }

    public Door_Sensor getDoor_sensor() {
        return door_sensor;
    }

    public void setDoor_sensor(Door_Sensor door_sensor) {
        this.door_sensor = door_sensor;
    }

}