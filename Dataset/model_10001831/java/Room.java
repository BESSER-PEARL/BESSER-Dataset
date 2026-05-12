





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private None _nurs;
    private String room_type;
    private int capasittity;
    private String patients;
    private boolean available;
    private int num;





    private Patient patient;




    private nurse nurse;


    public Room(
        None _nurs,        String room_type,        int capasittity,        String patients,        boolean available,        int num    ) {
        this._nurs = _nurs;
        this.room_type = room_type;
        this.capasittity = capasittity;
        this.patients = patients;
        this.available = available;
        this.num = num;
    }


    public None get_nurs() {
        return _nurs;
    }

    public void set_nurs(None _nurs) {
        this._nurs = _nurs;
    }
    public String getRoom_type() {
        return room_type;
    }

    public void setRoom_type(String room_type) {
        this.room_type = room_type;
    }
    public int getCapasittity() {
        return capasittity;
    }

    public void setCapasittity(int capasittity) {
        this.capasittity = capasittity;
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
    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
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