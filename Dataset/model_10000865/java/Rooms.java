





import java.util.List;
import java.util.ArrayList;

public class Rooms  {

    private String location;
    private int Roomno;





    private Patient patient;


    public Rooms(
        String location,        int Roomno    ) {
        this.location = location;
        this.Roomno = Roomno;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public int getRoomno() {
        return Roomno;
    }

    public void setRoomno(int Roomno) {
        this.Roomno = Roomno;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}