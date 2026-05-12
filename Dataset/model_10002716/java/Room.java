





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private String location;
    private int roomno;





    private List<Patient> patients;


    public Room(
        String location,        int roomno    ) {
        this.location = location;
        this.roomno = roomno;
        this.patients = new ArrayList<>();
    }

    public Room(
        String location,        int roomno        ArrayList<Patient> patients    ) {
        this.location = location;
        this.roomno = roomno;
        this.patients = patients;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public int getRoomno() {
        return roomno;
    }

    public void setRoomno(int roomno) {
        this.roomno = roomno;
    }

    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}