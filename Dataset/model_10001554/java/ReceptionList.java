





import java.util.List;
import java.util.ArrayList;

public class ReceptionList  {

    private int RepId;
    private String name;





    private List<Patient> patients;


    public ReceptionList(
        int RepId,        String name    ) {
        this.RepId = RepId;
        this.name = name;
        this.patients = new ArrayList<>();
    }

    public ReceptionList(
        int RepId,        String name        ArrayList<Patient> patients    ) {
        this.RepId = RepId;
        this.name = name;
        this.patients = patients;
    }

    public int getRepid() {
        return RepId;
    }

    public void setRepid(int RepId) {
        this.RepId = RepId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}