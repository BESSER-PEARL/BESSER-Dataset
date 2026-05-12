





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private int RoomNo;
    private String RoomType;





    private Patient patient;


    public Room(
        int RoomNo,        String RoomType    ) {
        this.RoomNo = RoomNo;
        this.RoomType = RoomType;
    }


    public int getRoomno() {
        return RoomNo;
    }

    public void setRoomno(int RoomNo) {
        this.RoomNo = RoomNo;
    }
    public String getRoomtype() {
        return RoomType;
    }

    public void setRoomtype(String RoomType) {
        this.RoomType = RoomType;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}