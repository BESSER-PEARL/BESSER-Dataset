





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private String RoomType;
    private int RoomNo;





    private Patient patient;


    public Room(
        String RoomType,        int RoomNo    ) {
        this.RoomType = RoomType;
        this.RoomNo = RoomNo;
    }


    public String getRoomtype() {
        return RoomType;
    }

    public void setRoomtype(String RoomType) {
        this.RoomType = RoomType;
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