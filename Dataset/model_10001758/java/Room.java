





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private int Room_NO;
    private String Room_TYPE;
    private String Room_Rent;





    private List<patient> patients;




    private Nurse nurse;


    public Room(
        int Room_NO,        String Room_TYPE,        String Room_Rent    ) {
        this.Room_NO = Room_NO;
        this.Room_TYPE = Room_TYPE;
        this.Room_Rent = Room_Rent;
        this.patients = new ArrayList<>();
    }

    public Room(
        int Room_NO,        String Room_TYPE,        String Room_Rent        ArrayList<patient> patients    ) {
        this.Room_NO = Room_NO;
        this.Room_TYPE = Room_TYPE;
        this.Room_Rent = Room_Rent;
        this.patients = patients;
    }

    public int getRoom_no() {
        return Room_NO;
    }

    public void setRoom_no(int Room_NO) {
        this.Room_NO = Room_NO;
    }
    public String getRoom_type() {
        return Room_TYPE;
    }

    public void setRoom_type(String Room_TYPE) {
        this.Room_TYPE = Room_TYPE;
    }
    public String getRoom_rent() {
        return Room_Rent;
    }

    public void setRoom_rent(String Room_Rent) {
        this.Room_Rent = Room_Rent;
    }

    public List<patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }
    public Nurse getNurse() {
        return nurse;
    }

    public void setNurse(Nurse nurse) {
        this.nurse = nurse;
    }

}