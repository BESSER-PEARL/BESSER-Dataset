





import java.util.List;
import java.util.ArrayList;

public class Operation_Staff  {

    private String DoctorLocation;
    private String NurseName;
    private String DoctorSpeciality;





    private List<Patient> patients;


    public Operation_Staff(
        String DoctorLocation,        String NurseName,        String DoctorSpeciality    ) {
        this.DoctorLocation = DoctorLocation;
        this.NurseName = NurseName;
        this.DoctorSpeciality = DoctorSpeciality;
        this.patients = new ArrayList<>();
    }

    public Operation_Staff(
        String DoctorLocation,        String NurseName,        String DoctorSpeciality        ArrayList<Patient> patients    ) {
        this.DoctorLocation = DoctorLocation;
        this.NurseName = NurseName;
        this.DoctorSpeciality = DoctorSpeciality;
        this.patients = patients;
    }

    public String getDoctorlocation() {
        return DoctorLocation;
    }

    public void setDoctorlocation(String DoctorLocation) {
        this.DoctorLocation = DoctorLocation;
    }
    public String getNursename() {
        return NurseName;
    }

    public void setNursename(String NurseName) {
        this.NurseName = NurseName;
    }
    public String getDoctorspeciality() {
        return DoctorSpeciality;
    }

    public void setDoctorspeciality(String DoctorSpeciality) {
        this.DoctorSpeciality = DoctorSpeciality;
    }

    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}