





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String employeeSurname;
    private String employeeName;
    private String employeePassword;
    private int employeeID;
    private String employeeUsername;
    private String employeeEmail;
    private String employeeMobile;
    private String employeeAddress;



    public Employee(
        String employeeSurname,        String employeeName,        String employeePassword,        int employeeID,        String employeeUsername,        String employeeEmail,        String employeeMobile,        String employeeAddress    ) {
        this.employeeSurname = employeeSurname;
        this.employeeName = employeeName;
        this.employeePassword = employeePassword;
        this.employeeID = employeeID;
        this.employeeUsername = employeeUsername;
        this.employeeEmail = employeeEmail;
        this.employeeMobile = employeeMobile;
        this.employeeAddress = employeeAddress;
    }


    public String getEmployeesurname() {
        return employeeSurname;
    }

    public void setEmployeesurname(String employeeSurname) {
        this.employeeSurname = employeeSurname;
    }
    public String getEmployeename() {
        return employeeName;
    }

    public void setEmployeename(String employeeName) {
        this.employeeName = employeeName;
    }
    public String getEmployeepassword() {
        return employeePassword;
    }

    public void setEmployeepassword(String employeePassword) {
        this.employeePassword = employeePassword;
    }
    public int getEmployeeid() {
        return employeeID;
    }

    public void setEmployeeid(int employeeID) {
        this.employeeID = employeeID;
    }
    public String getEmployeeusername() {
        return employeeUsername;
    }

    public void setEmployeeusername(String employeeUsername) {
        this.employeeUsername = employeeUsername;
    }
    public String getEmployeeemail() {
        return employeeEmail;
    }

    public void setEmployeeemail(String employeeEmail) {
        this.employeeEmail = employeeEmail;
    }
    public String getEmployeemobile() {
        return employeeMobile;
    }

    public void setEmployeemobile(String employeeMobile) {
        this.employeeMobile = employeeMobile;
    }
    public String getEmployeeaddress() {
        return employeeAddress;
    }

    public void setEmployeeaddress(String employeeAddress) {
        this.employeeAddress = employeeAddress;
    }


}