





import java.util.List;
import java.util.ArrayList;

public class Entry_Points  {

    private int DoorID;





    private IoT_based_Smart_Resort_System iot_based_smart_resort_system;




    private List<Doors> doorss;




    private List<Windows> windowss;


    public Entry_Points(
        int DoorID    ) {
        this.DoorID = DoorID;
        this.doorss = new ArrayList<>();
        this.windowss = new ArrayList<>();
    }

    public Entry_Points(
        int DoorID        ArrayList<Doors> doorss,        ArrayList<Windows> windowss    ) {
        this.DoorID = DoorID;
        this.doorss = doorss;
        this.windowss = windowss;
    }

    public int getDoorid() {
        return DoorID;
    }

    public void setDoorid(int DoorID) {
        this.DoorID = DoorID;
    }

    public IoT_based_Smart_Resort_System getIot_based_smart_resort_system() {
        return iot_based_smart_resort_system;
    }

    public void setIot_based_smart_resort_system(IoT_based_Smart_Resort_System iot_based_smart_resort_system) {
        this.iot_based_smart_resort_system = iot_based_smart_resort_system;
    }
    public List<Doors> getDoorss() {
        return doorss;
    }

    public void addDoors(Doors doors) {
        this.doorss.add(doors);
    }
    public List<Windows> getWindowss() {
        return windowss;
    }

    public void addWindows(Windows windows) {
        this.windowss.add(windows);
    }

}