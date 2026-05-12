





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String lastname;
    private String firstname;





    private Patient patient;


    public Receptionist(
        String lastname,        String firstname    ) {
        this.lastname = lastname;
        this.firstname = firstname;
    }


    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}