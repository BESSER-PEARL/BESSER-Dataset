





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String specialization;
    private int phno;
    private String department;
    private String name;
    private int docid;
    private String address;





    private List<Patient> patients;




    private Department department;


    public Doctor(
        String specialization,        int phno,        String department,        String name,        int docid,        String address    ) {
        this.specialization = specialization;
        this.phno = phno;
        this.department = department;
        this.name = name;
        this.docid = docid;
        this.address = address;
        this.patients = new ArrayList<>();
    }

    public Doctor(
        String specialization,        int phno,        String department,        String name,        int docid,        String address        ArrayList<Patient> patients    ) {
        this.specialization = specialization;
        this.phno = phno;
        this.department = department;
        this.name = name;
        this.docid = docid;
        this.address = address;
        this.patients = patients;
    }

    public String getSpecialization() {
        return specialization;
    }

    public void setSpecialization(String specialization) {
        this.specialization = specialization;
    }
    public int getPhno() {
        return phno;
    }

    public void setPhno(int phno) {
        this.phno = phno;
    }
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getDocid() {
        return docid;
    }

    public void setDocid(int docid) {
        this.docid = docid;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }
    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

}