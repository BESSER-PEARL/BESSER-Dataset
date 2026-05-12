





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private int capasittity;
    private int num;
    private String patients;
    private boolean available;
    private String room_type;





    private Patient patient;




    private nurse nurse;


    public Room(
        int capasittity,        int num,        String patients,        boolean available,        String room_type    ) {
        this.capasittity = capasittity;
        this.num = num;
        this.patients = patients;
        this.available = available;
        this.room_type = room_type;
    }


    public int getCapasittity() {
        return capasittity;
    }

    public void setCapasittity(int capasittity) {
        this.capasittity = capasittity;
    }
    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }
    public String getPatients() {
        return patients;
    }

    public void setPatients(String patients) {
        this.patients = patients;
    }
    public boolean getAvailable() {
        return available;
    }

    public void setAvailable(boolean available) {
        this.available = available;
    }
    public String getRoom_type() {
        return room_type;
    }

    public void setRoom_type(String room_type) {
        this.room_type = room_type;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }
    public nurse getNurse() {
        return nurse;
    }

    public void setNurse(nurse nurse) {
        this.nurse = nurse;
    }

}