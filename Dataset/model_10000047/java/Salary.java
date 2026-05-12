





import java.util.List;
import java.util.ArrayList;

public class Salary  {

    private String Salary;
    private String position;
    private int id;





    private Employee employee;


    public Salary(
        String Salary,        String position,        int id    ) {
        this.Salary = Salary;
        this.position = position;
        this.id = id;
    }


    public String getSalary() {
        return Salary;
    }

    public void setSalary(String Salary) {
        this.Salary = Salary;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}