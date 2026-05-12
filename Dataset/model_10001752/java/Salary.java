





import java.util.List;
import java.util.ArrayList;

public class Salary  {

    private String position;
    private String Salary;
    private int id;





    private Employee employee;


    public Salary(
        String position,        String Salary,        int id    ) {
        this.position = position;
        this.Salary = Salary;
        this.id = id;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getSalary() {
        return Salary;
    }

    public void setSalary(String Salary) {
        this.Salary = Salary;
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