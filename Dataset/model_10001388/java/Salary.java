





import java.util.List;
import java.util.ArrayList;

public class Salary  {

    private String basic_salary;
    private int emp_id;
    private String emp_name;





    private Employee employee;


    public Salary(
        String basic_salary,        int emp_id,        String emp_name    ) {
        this.basic_salary = basic_salary;
        this.emp_id = emp_id;
        this.emp_name = emp_name;
    }


    public String getBasic_salary() {
        return basic_salary;
    }

    public void setBasic_salary(String basic_salary) {
        this.basic_salary = basic_salary;
    }
    public int getEmp_id() {
        return emp_id;
    }

    public void setEmp_id(int emp_id) {
        this.emp_id = emp_id;
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