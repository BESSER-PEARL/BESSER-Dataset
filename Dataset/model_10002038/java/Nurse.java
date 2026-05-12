





import java.util.List;
import java.util.ArrayList;

public class Nurse  {

    private String Name;
    private int ID;





    private Patient patient;




    private Doctor doctor;


    public Nurse(
        String Name,        int ID    ) {
        this.Name = Name;
        this.ID = ID;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }
    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }

}