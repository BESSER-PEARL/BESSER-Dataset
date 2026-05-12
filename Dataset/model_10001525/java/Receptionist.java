





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String Email;
    private String Name;
    private int Id;





    private Patient patient;


    public Receptionist(
        String Email,        String Name,        int Id    ) {
        this.Email = Email;
        this.Name = Name;
        this.Id = Id;
    }


    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
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

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}