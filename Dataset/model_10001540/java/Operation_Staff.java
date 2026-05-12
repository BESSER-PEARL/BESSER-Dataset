





import java.util.List;
import java.util.ArrayList;

public class Operation_Staff  {

    private String DoctorSpeciality;
    private String NurseName;
    private String DoctorLocation;





    private List<Patient> patients;


    public Operation_Staff(
        String DoctorSpeciality,        String NurseName,        String DoctorLocation    ) {
        this.DoctorSpeciality = DoctorSpeciality;
        this.NurseName = NurseName;
        this.DoctorLocation = DoctorLocation;
        this.patients = new ArrayList<>();
    }

    public Operation_Staff(
        String DoctorSpeciality,        String NurseName,        String DoctorLocation        ArrayList<Patient> patients    ) {
        this.DoctorSpeciality = DoctorSpeciality;
        this.NurseName = NurseName;
        this.DoctorLocation = DoctorLocation;
        this.patients = patients;
    }

    public String getDoctorspeciality() {
        return DoctorSpeciality;
    }

    public void setDoctorspeciality(String DoctorSpeciality) {
        this.DoctorSpeciality = DoctorSpeciality;
    }
    public String getNursename() {
        return NurseName;
    }

    public void setNursename(String NurseName) {
        this.NurseName = NurseName;
    }
    public String getDoctorlocation() {
        return DoctorLocation;
    }

    public void setDoctorlocation(String DoctorLocation) {
        this.DoctorLocation = DoctorLocation;
    }

    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}