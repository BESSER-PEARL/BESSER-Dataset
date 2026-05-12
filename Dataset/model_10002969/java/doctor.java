





import java.util.List;
import java.util.ArrayList;

public class doctor  {

    private String phone_no;
    private String dept;
    private String specilization;
    private String name;
    private String did;





    private List<patient> patients;


    public doctor(
        String phone_no,        String dept,        String specilization,        String name,        String did    ) {
        this.phone_no = phone_no;
        this.dept = dept;
        this.specilization = specilization;
        this.name = name;
        this.did = did;
        this.patients = new ArrayList<>();
    }

    public doctor(
        String phone_no,        String dept,        String specilization,        String name,        String did        ArrayList<patient> patients    ) {
        this.phone_no = phone_no;
        this.dept = dept;
        this.specilization = specilization;
        this.name = name;
        this.did = did;
        this.patients = patients;
    }

    public String getPhone_no() {
        return phone_no;
    }

    public void setPhone_no(String phone_no) {
        this.phone_no = phone_no;
    }
    public String getDept() {
        return dept;
    }

    public void setDept(String dept) {
        this.dept = dept;
    }
    public String getSpecilization() {
        return specilization;
    }

    public void setSpecilization(String specilization) {
        this.specilization = specilization;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDid() {
        return did;
    }

    public void setDid(String did) {
        this.did = did;
    }

    public List<patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}