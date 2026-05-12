





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private String roomtype;
    private int roomno;





    private Patient patient;


    public Room(
        String roomtype,        int roomno    ) {
        this.roomtype = roomtype;
        this.roomno = roomno;
    }


    public String getRoomtype() {
        return roomtype;
    }

    public void setRoomtype(String roomtype) {
        this.roomtype = roomtype;
    }
    public int getRoomno() {
        return roomno;
    }

    public void setRoomno(int roomno) {
        this.roomno = roomno;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}