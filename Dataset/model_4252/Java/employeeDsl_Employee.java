





import java.util.List;
import java.util.ArrayList;

public class employeeDsl_Employee  {

    private int salary;
    private int ID;
    private String name;





    private employeeDsl_EmployeeContainer employeedsl_employeecontainer;


    public employeeDsl_Employee(
        int salary,        int ID,        String name    ) {
        this.salary = salary;
        this.ID = ID;
        this.name = name;
    }


    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public employeeDsl_EmployeeContainer getEmployeedsl_employeecontainer() {
        return employeedsl_employeecontainer;
    }

    public void setEmployeedsl_employeecontainer(employeeDsl_EmployeeContainer employeedsl_employeecontainer) {
        this.employeedsl_employeecontainer = employeedsl_employeecontainer;
    }

}