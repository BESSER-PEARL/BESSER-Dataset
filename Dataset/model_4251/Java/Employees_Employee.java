





import java.util.List;
import java.util.ArrayList;

public class Employees_Employee  {

    private String name;
    private int ID;
    private int salary;





    private Employees_EmployeeContainer employees_employeecontainer;


    public Employees_Employee(
        String name,        int ID,        int salary    ) {
        this.name = name;
        this.ID = ID;
        this.salary = salary;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    public Employees_EmployeeContainer getEmployees_employeecontainer() {
        return employees_employeecontainer;
    }

    public void setEmployees_employeecontainer(Employees_EmployeeContainer employees_employeecontainer) {
        this.employees_employeecontainer = employees_employeecontainer;
    }

}