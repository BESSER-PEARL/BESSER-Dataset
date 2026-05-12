





import java.util.List;
import java.util.ArrayList;

public class Rooms  {

    private int RoomNo;
    private String Location;





    private Patient patient;


    public Rooms(
        int RoomNo,        String Location    ) {
        this.RoomNo = RoomNo;
        this.Location = Location;
    }


    public int getRoomno() {
        return RoomNo;
    }

    public void setRoomno(int RoomNo) {
        this.RoomNo = RoomNo;
    }
    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}