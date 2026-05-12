





import java.util.List;
import java.util.ArrayList;

public class Salary  {

    private int DaysAttended;
    private String EmployeeID;
    private int NetSalary;
    private int Bonus;





    private Employee employee;


    public Salary(
        int DaysAttended,        String EmployeeID,        int NetSalary,        int Bonus    ) {
        this.DaysAttended = DaysAttended;
        this.EmployeeID = EmployeeID;
        this.NetSalary = NetSalary;
        this.Bonus = Bonus;
    }


    public int getDaysattended() {
        return DaysAttended;
    }

    public void setDaysattended(int DaysAttended) {
        this.DaysAttended = DaysAttended;
    }
    public String getEmployeeid() {
        return EmployeeID;
    }

    public void setEmployeeid(String EmployeeID) {
        this.EmployeeID = EmployeeID;
    }
    public int getNetsalary() {
        return NetSalary;
    }

    public void setNetsalary(int NetSalary) {
        this.NetSalary = NetSalary;
    }
    public int getBonus() {
        return Bonus;
    }

    public void setBonus(int Bonus) {
        this.Bonus = Bonus;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}