





import java.util.List;
import java.util.ArrayList;

public class Employee_DB  {

    private None Name__1st_and_last_;
    private String Password;
    private String E_Mail;
    private None Title;
    private None Supervisor;
    private None Username;
    private int Salary;
    private int Employee_ID;
    private int Telephone;
    private int Date_of_Birth;
    private int SSN;
    private String Address;



    public Employee_DB(
        None Name__1st_and_last_,        String Password,        String E_Mail,        None Title,        None Supervisor,        None Username,        int Salary,        int Employee_ID,        int Telephone,        int Date_of_Birth,        int SSN,        String Address    ) {
        this.Name__1st_and_last_ = Name__1st_and_last_;
        this.Password = Password;
        this.E_Mail = E_Mail;
        this.Title = Title;
        this.Supervisor = Supervisor;
        this.Username = Username;
        this.Salary = Salary;
        this.Employee_ID = Employee_ID;
        this.Telephone = Telephone;
        this.Date_of_Birth = Date_of_Birth;
        this.SSN = SSN;
        this.Address = Address;
    }


    public None getName__1st_and_last_() {
        return Name__1st_and_last_;
    }

    public void setName__1st_and_last_(None Name__1st_and_last_) {
        this.Name__1st_and_last_ = Name__1st_and_last_;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getE_mail() {
        return E_Mail;
    }

    public void setE_mail(String E_Mail) {
        this.E_Mail = E_Mail;
    }
    public None getTitle() {
        return Title;
    }

    public void setTitle(None Title) {
        this.Title = Title;
    }
    public None getSupervisor() {
        return Supervisor;
    }

    public void setSupervisor(None Supervisor) {
        this.Supervisor = Supervisor;
    }
    public None getUsername() {
        return Username;
    }

    public void setUsername(None Username) {
        this.Username = Username;
    }
    public int getSalary() {
        return Salary;
    }

    public void setSalary(int Salary) {
        this.Salary = Salary;
    }
    public int getEmployee_id() {
        return Employee_ID;
    }

    public void setEmployee_id(int Employee_ID) {
        this.Employee_ID = Employee_ID;
    }
    public int getTelephone() {
        return Telephone;
    }

    public void setTelephone(int Telephone) {
        this.Telephone = Telephone;
    }
    public int getDate_of_birth() {
        return Date_of_Birth;
    }

    public void setDate_of_birth(int Date_of_Birth) {
        this.Date_of_Birth = Date_of_Birth;
    }
    public int getSsn() {
        return SSN;
    }

    public void setSsn(int SSN) {
        this.SSN = SSN;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }


}