





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String Location;
    private String Specialization;
    private int Docid;
    private String DocName;
    private String Phoneno;
    private String Dept;





    private List<Patient> patients;




    private Dept dept;


    public Doctor(
        String Location,        String Specialization,        int Docid,        String DocName,        String Phoneno,        String Dept    ) {
        this.Location = Location;
        this.Specialization = Specialization;
        this.Docid = Docid;
        this.DocName = DocName;
        this.Phoneno = Phoneno;
        this.Dept = Dept;
        this.patients = new ArrayList<>();
    }

    public Doctor(
        String Location,        String Specialization,        int Docid,        String DocName,        String Phoneno,        String Dept        ArrayList<Patient> patients    ) {
        this.Location = Location;
        this.Specialization = Specialization;
        this.Docid = Docid;
        this.DocName = DocName;
        this.Phoneno = Phoneno;
        this.Dept = Dept;
        this.patients = patients;
    }

    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }
    public String getSpecialization() {
        return Specialization;
    }

    public void setSpecialization(String Specialization) {
        this.Specialization = Specialization;
    }
    public int getDocid() {
        return Docid;
    }

    public void setDocid(int Docid) {
        this.Docid = Docid;
    }
    public String getDocname() {
        return DocName;
    }

    public void setDocname(String DocName) {
        this.DocName = DocName;
    }
    public String getPhoneno() {
        return Phoneno;
    }

    public void setPhoneno(String Phoneno) {
        this.Phoneno = Phoneno;
    }
    public String getDept() {
        return Dept;
    }

    public void setDept(String Dept) {
        this.Dept = Dept;
    }

    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }
    public Dept getDept() {
        return dept;
    }

    public void setDept(Dept dept) {
        this.dept = dept;
    }

}