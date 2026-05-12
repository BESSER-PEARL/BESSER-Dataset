




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class employee  {

    private LocalDate Date_Started;
    private float workingHours;
    private None Department;
    private String empid;
    private LocalDate Date_Hired;
    private LocalDate Date_Ended;
    private String ssn;
    private None Role;





    private account account;


    public employee(
        LocalDate Date_Started,        float workingHours,        None Department,        String empid,        LocalDate Date_Hired,        LocalDate Date_Ended,        String ssn,        None Role    ) {
        this.Date_Started = Date_Started;
        this.workingHours = workingHours;
        this.Department = Department;
        this.empid = empid;
        this.Date_Hired = Date_Hired;
        this.Date_Ended = Date_Ended;
        this.ssn = ssn;
        this.Role = Role;
    }


    public LocalDate getDate_started() {
        return Date_Started;
    }

    public void setDate_started(LocalDate Date_Started) {
        this.Date_Started = Date_Started;
    }
    public float getWorkinghours() {
        return workingHours;
    }

    public void setWorkinghours(float workingHours) {
        this.workingHours = workingHours;
    }
    public None getDepartment() {
        return Department;
    }

    public void setDepartment(None Department) {
        this.Department = Department;
    }
    public String getEmpid() {
        return empid;
    }

    public void setEmpid(String empid) {
        this.empid = empid;
    }
    public LocalDate getDate_hired() {
        return Date_Hired;
    }

    public void setDate_hired(LocalDate Date_Hired) {
        this.Date_Hired = Date_Hired;
    }
    public LocalDate getDate_ended() {
        return Date_Ended;
    }

    public void setDate_ended(LocalDate Date_Ended) {
        this.Date_Ended = Date_Ended;
    }
    public String getSsn() {
        return ssn;
    }

    public void setSsn(String ssn) {
        this.ssn = ssn;
    }
    public None getRole() {
        return Role;
    }

    public void setRole(None Role) {
        this.Role = Role;
    }

    public account getAccount() {
        return account;
    }

    public void setAccount(account account) {
        this.account = account;
    }

}