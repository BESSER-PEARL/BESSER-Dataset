





import java.util.List;
import java.util.ArrayList;

public class Receiptionist  {






    private List<patient> patients;


    public Receiptionist(
    ) {
        this.patients = new ArrayList<>();
    }

    public Receiptionist(
        ArrayList<patient> patients    ) {
        this.patients = patients;
    }


    public List<patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}