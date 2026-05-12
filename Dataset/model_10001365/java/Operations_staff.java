





import java.util.List;
import java.util.ArrayList;

public class Operations_staff  {






    private List<Patient> patients;


    public Operations_staff(
    ) {
        this.patients = new ArrayList<>();
    }

    public Operations_staff(
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