





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String Specialization;
    private int docId;
    private int PhoneNo;
    private String Name;
    private String Dept;
    private String Location;





    private Dept dept;




    private List<Patient> patients;


    public Doctor(
        String Specialization,        int docId,        int PhoneNo,        String Name,        String Dept,        String Location    ) {
        this.Specialization = Specialization;
        this.docId = docId;
        this.PhoneNo = PhoneNo;
        this.Name = Name;
        this.Dept = Dept;
        this.Location = Location;
        this.patients = new ArrayList<>();
    }

    public Doctor(
        String Specialization,        int docId,        int PhoneNo,        String Name,        String Dept,        String Location        ArrayList<Patient> patients    ) {
        this.Specialization = Specialization;
        this.docId = docId;
        this.PhoneNo = PhoneNo;
        this.Name = Name;
        this.Dept = Dept;
        this.Location = Location;
        this.patients = patients;
    }

    public String getSpecialization() {
        return Specialization;
    }

    public void setSpecialization(String Specialization) {
        this.Specialization = Specialization;
    }
    public int getDocid() {
        return docId;
    }

    public void setDocid(int docId) {
        this.docId = docId;
    }
    public int getPhoneno() {
        return PhoneNo;
    }

    public void setPhoneno(int PhoneNo) {
        this.PhoneNo = PhoneNo;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDept() {
        return Dept;
    }

    public void setDept(String Dept) {
        this.Dept = Dept;
    }
    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }

    public Dept getDept() {
        return dept;
    }

    public void setDept(Dept dept) {
        this.dept = dept;
    }
    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}