





import java.util.List;
import java.util.ArrayList;

public class Employee_DB  {

    private int Telephone;
    private None Title;
    private int SSN;
    private String E_Mail;
    private None Name__1st_and_last_;
    private int Salary;
    private String Password;
    private String Address;
    private int Employee_ID;
    private None Username;
    private None Supervisor;
    private int Date_of_Birth;





    private Employee_Title__Non_Admin employee_title__non_admin;


    public Employee_DB(
        int Telephone,        None Title,        int SSN,        String E_Mail,        None Name__1st_and_last_,        int Salary,        String Password,        String Address,        int Employee_ID,        None Username,        None Supervisor,        int Date_of_Birth    ) {
        this.Telephone = Telephone;
        this.Title = Title;
        this.SSN = SSN;
        this.E_Mail = E_Mail;
        this.Name__1st_and_last_ = Name__1st_and_last_;
        this.Salary = Salary;
        this.Password = Password;
        this.Address = Address;
        this.Employee_ID = Employee_ID;
        this.Username = Username;
        this.Supervisor = Supervisor;
        this.Date_of_Birth = Date_of_Birth;
    }


    public int getTelephone() {
        return Telephone;
    }

    public void setTelephone(int Telephone) {
        this.Telephone = Telephone;
    }
    public None getTitle() {
        return Title;
    }

    public void setTitle(None Title) {
        this.Title = Title;
    }
    public int getSsn() {
        return SSN;
    }

    public void setSsn(int SSN) {
        this.SSN = SSN;
    }
    public String getE_mail() {
        return E_Mail;
    }

    public void setE_mail(String E_Mail) {
        this.E_Mail = E_Mail;
    }
    public None getName__1st_and_last_() {
        return Name__1st_and_last_;
    }

    public void setName__1st_and_last_(None Name__1st_and_last_) {
        this.Name__1st_and_last_ = Name__1st_and_last_;
    }
    public int getSalary() {
        return Salary;
    }

    public void setSalary(int Salary) {
        this.Salary = Salary;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getEmployee_id() {
        return Employee_ID;
    }

    public void setEmployee_id(int Employee_ID) {
        this.Employee_ID = Employee_ID;
    }
    public None getUsername() {
        return Username;
    }

    public void setUsername(None Username) {
        this.Username = Username;
    }
    public None getSupervisor() {
        return Supervisor;
    }

    public void setSupervisor(None Supervisor) {
        this.Supervisor = Supervisor;
    }
    public int getDate_of_birth() {
        return Date_of_Birth;
    }

    public void setDate_of_birth(int Date_of_Birth) {
        this.Date_of_Birth = Date_of_Birth;
    }

    public Employee_Title__Non_Admin getEmployee_title__non_admin() {
        return employee_title__non_admin;
    }

    public void setEmployee_title__non_admin(Employee_Title__Non_Admin employee_title__non_admin) {
        this.employee_title__non_admin = employee_title__non_admin;
    }

}