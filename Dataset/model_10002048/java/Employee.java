





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private int EmpID;
    private String Department;
    private String Name;
    private String ContactNo;



    public Employee(
        int EmpID,        String Department,        String Name,        String ContactNo    ) {
        this.EmpID = EmpID;
        this.Department = Department;
        this.Name = Name;
        this.ContactNo = ContactNo;
    }


    public int getEmpid() {
        return EmpID;
    }

    public void setEmpid(int EmpID) {
        this.EmpID = EmpID;
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
    public String getContactno() {
        return ContactNo;
    }

    public void setContactno(String ContactNo) {
        this.ContactNo = ContactNo;
    }


}