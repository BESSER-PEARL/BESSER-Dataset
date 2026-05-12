





import java.util.List;
import java.util.ArrayList;

public class Rooms  {

    private String Location;
    private int RoomNo;





    private Patient patient;


    public Rooms(
        String Location,        int RoomNo    ) {
        this.Location = Location;
        this.RoomNo = RoomNo;
    }


    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }
    public int getRoomno() {
        return RoomNo;
    }

    public void setRoomno(int RoomNo) {
        this.RoomNo = RoomNo;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}