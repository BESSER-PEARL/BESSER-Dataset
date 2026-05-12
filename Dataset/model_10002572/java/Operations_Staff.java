





import java.util.List;
import java.util.ArrayList;

public class Operations_Staff  {






    private List<Patient> patients;


    public Operations_Staff(
    ) {
        this.patients = new ArrayList<>();
    }

    public Operations_Staff(
        ArrayList<Patient> patients    ) {
        this.patients = patients;
    }


    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}