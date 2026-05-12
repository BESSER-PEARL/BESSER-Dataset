





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String Emp_Name;
    private String Joindate;
    private String Salary;
    private String Address;
    private int Contact_NO;
    private int Emp_ID;
    private String Designation;



    public Employee(
        String Emp_Name,        String Joindate,        String Salary,        String Address,        int Contact_NO,        int Emp_ID,        String Designation    ) {
        this.Emp_Name = Emp_Name;
        this.Joindate = Joindate;
        this.Salary = Salary;
        this.Address = Address;
        this.Contact_NO = Contact_NO;
        this.Emp_ID = Emp_ID;
        this.Designation = Designation;
    }


    public String getEmp_name() {
        return Emp_Name;
    }

    public void setEmp_name(String Emp_Name) {
        this.Emp_Name = Emp_Name;
    }
    public String getJoindate() {
        return Joindate;
    }

    public void setJoindate(String Joindate) {
        this.Joindate = Joindate;
    }
    public String getSalary() {
        return Salary;
    }

    public void setSalary(String Salary) {
        this.Salary = Salary;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getContact_no() {
        return Contact_NO;
    }

    public void setContact_no(int Contact_NO) {
        this.Contact_NO = Contact_NO;
    }
    public int getEmp_id() {
        return Emp_ID;
    }

    public void setEmp_id(int Emp_ID) {
        this.Emp_ID = Emp_ID;
    }
    public String getDesignation() {
        return Designation;
    }

    public void setDesignation(String Designation) {
        this.Designation = Designation;
    }


}