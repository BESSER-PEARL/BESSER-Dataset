





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String name;
    private None User_Name;
    private String Password;





    private List<Doctor> doctors;


    public Admin(
        String name,        None User_Name,        String Password    ) {
        this.name = name;
        this.User_Name = User_Name;
        this.Password = Password;
        this.doctors = new ArrayList<>();
    }

    public Admin(
        String name,        None User_Name,        String Password        ArrayList<Doctor> doctors    ) {
        this.name = name;
        this.User_Name = User_Name;
        this.Password = Password;
        this.doctors = doctors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getUser_name() {
        return User_Name;
    }

    public void setUser_name(None User_Name) {
        this.User_Name = User_Name;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}