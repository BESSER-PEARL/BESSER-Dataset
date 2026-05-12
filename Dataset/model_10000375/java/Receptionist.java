





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String Name;
    private int Id;
    private String Email;





    private Patient patient;


    public Receptionist(
        String Name,        int Id,        String Email    ) {
        this.Name = Name;
        this.Id = Id;
        this.Email = Email;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}