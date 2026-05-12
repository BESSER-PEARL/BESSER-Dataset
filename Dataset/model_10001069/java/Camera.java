





import java.util.List;
import java.util.ArrayList;

public class Camera  {

    private int CameraID;





    private Door door;


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

    public Door getDoor() {
        return door;
    }

    public void setDoor(Door door) {
        this.door = door;
    }

}