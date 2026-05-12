





import java.util.List;
import java.util.ArrayList;

public class Rooms  {

    private String WardNo;
    private int RoomNo;





    private Patient patient;


    public Rooms(
        String WardNo,        int RoomNo    ) {
        this.WardNo = WardNo;
        this.RoomNo = RoomNo;
    }


    public String getWardno() {
        return WardNo;
    }

    public void setWardno(String WardNo) {
        this.WardNo = WardNo;
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