





import java.util.List;
import java.util.ArrayList;

public class doctor  {

    private String specilization;
    private String did;
    private String dept;
    private String name;
    private String phone_no;





    private List<patient> patients;


    public doctor(
        String specilization,        String did,        String dept,        String name,        String phone_no    ) {
        this.specilization = specilization;
        this.did = did;
        this.dept = dept;
        this.name = name;
        this.phone_no = phone_no;
        this.patients = new ArrayList<>();
    }

    public doctor(
        String specilization,        String did,        String dept,        String name,        String phone_no        ArrayList<patient> patients    ) {
        this.specilization = specilization;
        this.did = did;
        this.dept = dept;
        this.name = name;
        this.phone_no = phone_no;
        this.patients = patients;
    }

    public String getSpecilization() {
        return specilization;
    }

    public void setSpecilization(String specilization) {
        this.specilization = specilization;
    }
    public String getDid() {
        return did;
    }

    public void setDid(String did) {
        this.did = did;
    }
    public String getDept() {
        return dept;
    }

    public void setDept(String dept) {
        this.dept = dept;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhone_no() {
        return phone_no;
    }

    public void setPhone_no(String phone_no) {
        this.phone_no = phone_no;
    }

    public List<patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}