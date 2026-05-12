





import java.util.List;
import java.util.ArrayList;

public class Days_Attended  {

    private int Total_no__of_workingdays;
    private int OverTime;
    private int Days_attended;
    private int EmployeeBasicSalary;
    private String EmployeeId;





    private Employee employee;




    private Salary salary;


    public Days_Attended(
        int Total_no__of_workingdays,        int OverTime,        int Days_attended,        int EmployeeBasicSalary,        String EmployeeId    ) {
        this.Total_no__of_workingdays = Total_no__of_workingdays;
        this.OverTime = OverTime;
        this.Days_attended = Days_attended;
        this.EmployeeBasicSalary = EmployeeBasicSalary;
        this.EmployeeId = EmployeeId;
    }


    public int getTotal_no__of_workingdays() {
        return Total_no__of_workingdays;
    }

    public void setTotal_no__of_workingdays(int Total_no__of_workingdays) {
        this.Total_no__of_workingdays = Total_no__of_workingdays;
    }
    public int getOvertime() {
        return OverTime;
    }

    public void setOvertime(int OverTime) {
        this.OverTime = OverTime;
    }
    public int getDays_attended() {
        return Days_attended;
    }

    public void setDays_attended(int Days_attended) {
        this.Days_attended = Days_attended;
    }
    public int getEmployeebasicsalary() {
        return EmployeeBasicSalary;
    }

    public void setEmployeebasicsalary(int EmployeeBasicSalary) {
        this.EmployeeBasicSalary = EmployeeBasicSalary;
    }
    public String getEmployeeid() {
        return EmployeeId;
    }

    public void setEmployeeid(String EmployeeId) {
        this.EmployeeId = EmployeeId;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }
    public Salary getSalary() {
        return salary;
    }

    public void setSalary(Salary salary) {
        this.salary = salary;
    }

}