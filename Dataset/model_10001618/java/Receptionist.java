





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String Name;
    private int ID;





    private List<Doctor> doctors;




    private Patient patient;


    public Receptionist(
        String Name,        int ID    ) {
        this.Name = Name;
        this.ID = ID;
        this.doctors = new ArrayList<>();
    }

    public Receptionist(
        String Name,        int ID        ArrayList<Doctor> doctors    ) {
        this.Name = Name;
        this.ID = ID;
        this.doctors = doctors;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }
    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}