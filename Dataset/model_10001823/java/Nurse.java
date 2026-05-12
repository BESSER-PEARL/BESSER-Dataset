





import java.util.List;
import java.util.ArrayList;

public class Nurse  {

    private String attribute2;
    private int id;





    private Patient patient;


    public Nurse(
        String attribute2,        int id    ) {
        this.attribute2 = attribute2;
        this.id = id;
    }


    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}