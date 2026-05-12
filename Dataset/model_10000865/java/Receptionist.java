





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String Name;
    private int id;





    private Patient patient;


    public Receptionist(
        String Name,        int id    ) {
        this.Name = Name;
        this.id = id;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
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