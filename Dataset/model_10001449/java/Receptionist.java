





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String CNIC;
    private String name;





    private List<Patients> patientss;


    public Receptionist(
        String CNIC,        String name    ) {
        this.CNIC = CNIC;
        this.name = name;
        this.patientss = new ArrayList<>();
    }

    public Receptionist(
        String CNIC,        String name        ArrayList<Patients> patientss    ) {
        this.CNIC = CNIC;
        this.name = name;
        this.patientss = patientss;
    }

    public String getCnic() {
        return CNIC;
    }

    public void setCnic(String CNIC) {
        this.CNIC = CNIC;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Patients> getPatientss() {
        return patientss;
    }

    public void addPatients(Patients patients) {
        this.patientss.add(patients);
    }

}