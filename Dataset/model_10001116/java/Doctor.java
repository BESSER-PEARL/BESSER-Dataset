





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String Name;
    private int PhNo;
    private String Department;
    private int DocId;
    private String Specialization;



    public Doctor(
        String Name,        int PhNo,        String Department,        int DocId,        String Specialization    ) {
        this.Name = Name;
        this.PhNo = PhNo;
        this.Department = Department;
        this.DocId = DocId;
        this.Specialization = Specialization;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getPhno() {
        return PhNo;
    }

    public void setPhno(int PhNo) {
        this.PhNo = PhNo;
    }
    public String getDepartment() {
        return Department;
    }

    public void setDepartment(String Department) {
        this.Department = Department;
    }
    public int getDocid() {
        return DocId;
    }

    public void setDocid(int DocId) {
        this.DocId = DocId;
    }
    public String getSpecialization() {
        return Specialization;
    }

    public void setSpecialization(String Specialization) {
        this.Specialization = Specialization;
    }


}