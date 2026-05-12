





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String Type;
    private int Id;
    private String Name;





    private Patient patient;


    public Staff(
        String Type,        int Id,        String Name    ) {
        this.Type = Type;
        this.Id = Id;
        this.Name = Name;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}