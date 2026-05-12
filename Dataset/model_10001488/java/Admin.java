





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String uname;
    private String password;





    private List<Patient> patients;




    private List<Doctor> doctors;




    private user user;


    public Admin(
        String uname,        String password    ) {
        this.uname = uname;
        this.password = password;
        this.patients = new ArrayList<>();
        this.doctors = new ArrayList<>();
    }

    public Admin(
        String uname,        String password        ArrayList<Patient> patients,        ArrayList<Doctor> doctors    ) {
        this.uname = uname;
        this.password = password;
        this.patients = patients;
        this.doctors = doctors;
    }

    public String getUname() {
        return uname;
    }

    public void setUname(String uname) {
        this.uname = uname;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }
    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }
    public user getUser() {
        return user;
    }

    public void setUser(user user) {
        this.user = user;
    }

}