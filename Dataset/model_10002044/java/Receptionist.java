





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String email;
    private String username;
    private int id;
    private String password;





    private Patient patient;


    public Receptionist(
        String email,        String username,        int id,        String password    ) {
        this.email = email;
        this.username = username;
        this.id = id;
        this.password = password;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}