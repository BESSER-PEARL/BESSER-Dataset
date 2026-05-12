





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String Specialization;
    private String Address;
    private String Department;
    private String Name;
    private int DocID;
    private int PhNo;





    private List<Patient> patients;


    public Doctor(
        String Specialization,        String Address,        String Department,        String Name,        int DocID,        int PhNo    ) {
        this.Specialization = Specialization;
        this.Address = Address;
        this.Department = Department;
        this.Name = Name;
        this.DocID = DocID;
        this.PhNo = PhNo;
        this.patients = new ArrayList<>();
    }

    public Doctor(
        String Specialization,        String Address,        String Department,        String Name,        int DocID,        int PhNo        ArrayList<Patient> patients    ) {
        this.Specialization = Specialization;
        this.Address = Address;
        this.Department = Department;
        this.Name = Name;
        this.DocID = DocID;
        this.PhNo = PhNo;
        this.patients = patients;
    }

    public String getSpecialization() {
        return Specialization;
    }

    public void setSpecialization(String Specialization) {
        this.Specialization = Specialization;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getDepartment() {
        return Department;
    }

    public void setDepartment(String Department) {
        this.Department = Department;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getDocid() {
        return DocID;
    }

    public void setDocid(int DocID) {
        this.DocID = DocID;
    }
    public int getPhno() {
        return PhNo;
    }

    public void setPhno(int PhNo) {
        this.PhNo = PhNo;
    }

    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}