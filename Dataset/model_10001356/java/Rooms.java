





import java.util.List;
import java.util.ArrayList;

public class Rooms  {

    private int Room_No;
    private String Location;





    private List<Patient> patients;


    public Rooms(
        int Room_No,        String Location    ) {
        this.Room_No = Room_No;
        this.Location = Location;
        this.patients = new ArrayList<>();
    }

    public Rooms(
        int Room_No,        String Location        ArrayList<Patient> patients    ) {
        this.Room_No = Room_No;
        this.Location = Location;
        this.patients = patients;
    }

    public int getRoom_no() {
        return Room_No;
    }

    public void setRoom_no(int Room_No) {
        this.Room_No = Room_No;
    }
    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }

    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}