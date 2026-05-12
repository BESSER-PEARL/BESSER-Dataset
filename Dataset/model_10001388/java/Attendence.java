





import java.util.List;
import java.util.ArrayList;

public class Attendence  {

    private int emp_id;
    private int Basic_salary;
    private String emp_name;





    private Employee employee;


    public Attendence(
        int emp_id,        int Basic_salary,        String emp_name    ) {
        this.emp_id = emp_id;
        this.Basic_salary = Basic_salary;
        this.emp_name = emp_name;
    }


    public int getEmp_id() {
        return emp_id;
    }

    public void setEmp_id(int emp_id) {
        this.emp_id = emp_id;
    }
    public int getBasic_salary() {
        return Basic_salary;
    }

    public void setBasic_salary(int Basic_salary) {
        this.Basic_salary = Basic_salary;
    }
    public String getEmp_name() {
        return emp_name;
    }

    public void setEmp_name(String emp_name) {
        this.emp_name = emp_name;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}