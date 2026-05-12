





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String Name;
    private String Email;
    private int Id;





    private Patient patient;


    public Receptionist(
        String Name,        String Email,        int Id    ) {
        this.Name = Name;
        this.Email = Email;
        this.Id = Id;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}