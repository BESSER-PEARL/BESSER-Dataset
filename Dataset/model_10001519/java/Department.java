





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private String DocID;
    private String deptID;
    private String Name;





    private List<Doctor> doctors;


    public Department(
        String DocID,        String deptID,        String Name    ) {
        this.DocID = DocID;
        this.deptID = deptID;
        this.Name = Name;
        this.doctors = new ArrayList<>();
    }

    public Department(
        String DocID,        String deptID,        String Name        ArrayList<Doctor> doctors    ) {
        this.DocID = DocID;
        this.deptID = deptID;
        this.Name = Name;
        this.doctors = doctors;
    }

    public String getDocid() {
        return DocID;
    }

    public void setDocid(String DocID) {
        this.DocID = DocID;
    }
    public String getDeptid() {
        return deptID;
    }

    public void setDeptid(String deptID) {
        this.deptID = deptID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}