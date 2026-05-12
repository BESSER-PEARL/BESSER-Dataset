





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String Emp_Address;
    private String Emp_Name;
    private float Emp_Salary;
    private String Emp_ContactNo;
    private int Emp_Id;
    private String Emp_Department;
    private String Password;
    private String Emp_Email;



    public Employee(
        String Emp_Address,        String Emp_Name,        float Emp_Salary,        String Emp_ContactNo,        int Emp_Id,        String Emp_Department,        String Password,        String Emp_Email    ) {
        this.Emp_Address = Emp_Address;
        this.Emp_Name = Emp_Name;
        this.Emp_Salary = Emp_Salary;
        this.Emp_ContactNo = Emp_ContactNo;
        this.Emp_Id = Emp_Id;
        this.Emp_Department = Emp_Department;
        this.Password = Password;
        this.Emp_Email = Emp_Email;
    }


    public String getEmp_address() {
        return Emp_Address;
    }

    public void setEmp_address(String Emp_Address) {
        this.Emp_Address = Emp_Address;
    }
    public String getEmp_name() {
        return Emp_Name;
    }

    public void setEmp_name(String Emp_Name) {
        this.Emp_Name = Emp_Name;
    }
    public float getEmp_salary() {
        return Emp_Salary;
    }

    public void setEmp_salary(float Emp_Salary) {
        this.Emp_Salary = Emp_Salary;
    }
    public String getEmp_contactno() {
        return Emp_ContactNo;
    }

    public void setEmp_contactno(String Emp_ContactNo) {
        this.Emp_ContactNo = Emp_ContactNo;
    }
    public int getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(int Emp_Id) {
        this.Emp_Id = Emp_Id;
    }
    public String getEmp_department() {
        return Emp_Department;
    }

    public void setEmp_department(String Emp_Department) {
        this.Emp_Department = Emp_Department;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getEmp_email() {
        return Emp_Email;
    }

    public void setEmp_email(String Emp_Email) {
        this.Emp_Email = Emp_Email;
    }


}