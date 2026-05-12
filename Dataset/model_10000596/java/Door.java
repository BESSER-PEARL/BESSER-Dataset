





import java.util.List;
import java.util.ArrayList;

public class Door  {

    private int DoorID;





    private Sensor sensor;




    private List<Camera> cameras;


    public Door(
        int DoorID    ) {
        this.DoorID = DoorID;
        this.cameras = new ArrayList<>();
    }

    public Door(
        int DoorID        ArrayList<Camera> cameras    ) {
        this.DoorID = DoorID;
        this.cameras = cameras;
    }

    public int getDoorid() {
        return DoorID;
    }

    public void setDoorid(int DoorID) {
        this.DoorID = DoorID;
    }

    public Sensor getSensor() {
        return sensor;
    }

    public void setSensor(Sensor sensor) {
        this.sensor = sensor;
    }
    public List<Camera> getCameras() {
        return cameras;
    }

    public void addCamera(Camera camera) {
        this.cameras.add(camera);
    }

}