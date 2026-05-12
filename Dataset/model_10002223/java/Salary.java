





import java.util.List;
import java.util.ArrayList;

public class Salary  {

    private String Emp_Id;
    private String Bonus__;
    private int Days_attended;
    private String Net_Salary;





    private List<Employee> employees;




    private Employee employee;




    private DaysAttended daysattended;


    public Salary(
        String Emp_Id,        String Bonus__,        int Days_attended,        String Net_Salary    ) {
        this.Emp_Id = Emp_Id;
        this.Bonus__ = Bonus__;
        this.Days_attended = Days_attended;
        this.Net_Salary = Net_Salary;
        this.employees = new ArrayList<>();
    }

    public Salary(
        String Emp_Id,        String Bonus__,        int Days_attended,        String Net_Salary        ArrayList<Employee> employees    ) {
        this.Emp_Id = Emp_Id;
        this.Bonus__ = Bonus__;
        this.Days_attended = Days_attended;
        this.Net_Salary = Net_Salary;
        this.employees = employees;
    }

    public String getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(String Emp_Id) {
        this.Emp_Id = Emp_Id;
    }
    public String getBonus__() {
        return Bonus__;
    }

    public void setBonus__(String Bonus__) {
        this.Bonus__ = Bonus__;
    }
    public int getDays_attended() {
        return Days_attended;
    }

    public void setDays_attended(int Days_attended) {
        this.Days_attended = Days_attended;
    }
    public String getNet_salary() {
        return Net_Salary;
    }

    public void setNet_salary(String Net_Salary) {
        this.Net_Salary = Net_Salary;
    }

    public List<Employee> getEmployees() {
        return employees;
    }

    public void addEmployee(Employee employee) {
        this.employees.add(employee);
    }
    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }
    public DaysAttended getDaysattended() {
        return daysattended;
    }

    public void setDaysattended(DaysAttended daysattended) {
        this.daysattended = daysattended;
    }

}