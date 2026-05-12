





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String Emp_Email;
    private String Emp_ContactNo;
    private String Emp_Date_Of_Joint;
    private String Emp_Salary;
    private String Emp_Name;
    private String Emp_NIC;
    private String Emp_Department;
    private String Emp_Address;
    private None Emp_DOB;
    private String Emp_Position;
    private String Emp_Id;



    public Employee(
        String Emp_Email,        String Emp_ContactNo,        String Emp_Date_Of_Joint,        String Emp_Salary,        String Emp_Name,        String Emp_NIC,        String Emp_Department,        String Emp_Address,        None Emp_DOB,        String Emp_Position,        String Emp_Id    ) {
        this.Emp_Email = Emp_Email;
        this.Emp_ContactNo = Emp_ContactNo;
        this.Emp_Date_Of_Joint = Emp_Date_Of_Joint;
        this.Emp_Salary = Emp_Salary;
        this.Emp_Name = Emp_Name;
        this.Emp_NIC = Emp_NIC;
        this.Emp_Department = Emp_Department;
        this.Emp_Address = Emp_Address;
        this.Emp_DOB = Emp_DOB;
        this.Emp_Position = Emp_Position;
        this.Emp_Id = Emp_Id;
    }


    public String getEmp_email() {
        return Emp_Email;
    }

    public void setEmp_email(String Emp_Email) {
        this.Emp_Email = Emp_Email;
    }
    public String getEmp_contactno() {
        return Emp_ContactNo;
    }

    public void setEmp_contactno(String Emp_ContactNo) {
        this.Emp_ContactNo = Emp_ContactNo;
    }
    public String getEmp_date_of_joint() {
        return Emp_Date_Of_Joint;
    }

    public void setEmp_date_of_joint(String Emp_Date_Of_Joint) {
        this.Emp_Date_Of_Joint = Emp_Date_Of_Joint;
    }
    public String getEmp_salary() {
        return Emp_Salary;
    }

    public void setEmp_salary(String Emp_Salary) {
        this.Emp_Salary = Emp_Salary;
    }
    public String getEmp_name() {
        return Emp_Name;
    }

    public void setEmp_name(String Emp_Name) {
        this.Emp_Name = Emp_Name;
    }
    public String getEmp_nic() {
        return Emp_NIC;
    }

    public void setEmp_nic(String Emp_NIC) {
        this.Emp_NIC = Emp_NIC;
    }
    public String getEmp_department() {
        return Emp_Department;
    }

    public void setEmp_department(String Emp_Department) {
        this.Emp_Department = Emp_Department;
    }
    public String getEmp_address() {
        return Emp_Address;
    }

    public void setEmp_address(String Emp_Address) {
        this.Emp_Address = Emp_Address;
    }
    public None getEmp_dob() {
        return Emp_DOB;
    }

    public void setEmp_dob(None Emp_DOB) {
        this.Emp_DOB = Emp_DOB;
    }
    public String getEmp_position() {
        return Emp_Position;
    }

    public void setEmp_position(String Emp_Position) {
        this.Emp_Position = Emp_Position;
    }
    public String getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(String Emp_Id) {
        this.Emp_Id = Emp_Id;
    }


}