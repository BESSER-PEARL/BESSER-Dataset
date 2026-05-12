





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String phno;
    private int Docid;
    private String specialization;
    private String Department;
    private String Name;





    private Departmnt departmnt;




    private Patient patient;




    private Staff staff;


    public Doctor(
        String phno,        int Docid,        String specialization,        String Department,        String Name    ) {
        this.phno = phno;
        this.Docid = Docid;
        this.specialization = specialization;
        this.Department = Department;
        this.Name = Name;
    }


    public String getPhno() {
        return phno;
    }

    public void setPhno(String phno) {
        this.phno = phno;
    }
    public int getDocid() {
        return Docid;
    }

    public void setDocid(int Docid) {
        this.Docid = Docid;
    }
    public String getSpecialization() {
        return specialization;
    }

    public void setSpecialization(String specialization) {
        this.specialization = specialization;
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

    public Departmnt getDepartmnt() {
        return departmnt;
    }

    public void setDepartmnt(Departmnt departmnt) {
        this.departmnt = departmnt;
    }
    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }
    public Staff getStaff() {
        return staff;
    }

    public void setStaff(Staff staff) {
        this.staff = staff;
    }

}