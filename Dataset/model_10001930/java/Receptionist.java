





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private int Receptionid;
    private String RecName;





    private List<Patient> patients;


    public Receptionist(
        int Receptionid,        String RecName    ) {
        this.Receptionid = Receptionid;
        this.RecName = RecName;
        this.patients = new ArrayList<>();
    }

    public Receptionist(
        int Receptionid,        String RecName        ArrayList<Patient> patients    ) {
        this.Receptionid = Receptionid;
        this.RecName = RecName;
        this.patients = patients;
    }

    public int getReceptionid() {
        return Receptionid;
    }

    public void setReceptionid(int Receptionid) {
        this.Receptionid = Receptionid;
    }
    public String getRecname() {
        return RecName;
    }

    public void setRecname(String RecName) {
        this.RecName = RecName;
    }

    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}