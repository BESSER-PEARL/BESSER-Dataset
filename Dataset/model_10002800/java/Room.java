





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private int roomno;
    private String location;





    private List<Patient> patients;


    public Room(
        int roomno,        String location    ) {
        this.roomno = roomno;
        this.location = location;
        this.patients = new ArrayList<>();
    }

    public Room(
        int roomno,        String location        ArrayList<Patient> patients    ) {
        this.roomno = roomno;
        this.location = location;
        this.patients = patients;
    }

    public int getRoomno() {
        return roomno;
    }

    public void setRoomno(int roomno) {
        this.roomno = roomno;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}