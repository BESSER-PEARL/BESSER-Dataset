




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String Emp_Email;
    private String Emp_ContactNo;
    private LocalDate Emp_DOB;
    private String Emp_Name;
    private float Emp_Salary;
    private int Emp_Id;
    private String Emp_Designation;



    public Employee(
        String Emp_Email,        String Emp_ContactNo,        LocalDate Emp_DOB,        String Emp_Name,        float Emp_Salary,        int Emp_Id,        String Emp_Designation    ) {
        this.Emp_Email = Emp_Email;
        this.Emp_ContactNo = Emp_ContactNo;
        this.Emp_DOB = Emp_DOB;
        this.Emp_Name = Emp_Name;
        this.Emp_Salary = Emp_Salary;
        this.Emp_Id = Emp_Id;
        this.Emp_Designation = Emp_Designation;
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
    public LocalDate getEmp_dob() {
        return Emp_DOB;
    }

    public void setEmp_dob(LocalDate Emp_DOB) {
        this.Emp_DOB = Emp_DOB;
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
    public int getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(int Emp_Id) {
        this.Emp_Id = Emp_Id;
    }
    public String getEmp_designation() {
        return Emp_Designation;
    }

    public void setEmp_designation(String Emp_Designation) {
        this.Emp_Designation = Emp_Designation;
    }


}