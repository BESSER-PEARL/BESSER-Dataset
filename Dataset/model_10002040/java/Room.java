





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private String buildingname;
    private int no;
    private int floor;





    private Appointment appointment;


    public Room(
        String buildingname,        int no,        int floor    ) {
        this.buildingname = buildingname;
        this.no = no;
        this.floor = floor;
    }


    public String getBuildingname() {
        return buildingname;
    }

    public void setBuildingname(String buildingname) {
        this.buildingname = buildingname;
    }
    public int getNo() {
        return no;
    }

    public void setNo(int no) {
        this.no = no;
    }
    public int getFloor() {
        return floor;
    }

    public void setFloor(int floor) {
        this.floor = floor;
    }

    public Appointment getAppointment() {
        return appointment;
    }

    public void setAppointment(Appointment appointment) {
        this.appointment = appointment;
    }

}