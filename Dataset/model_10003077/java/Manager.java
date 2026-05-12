





import java.util.List;
import java.util.ArrayList;

public class Manager  {






    private List<Employee> employees;


    public Manager(
    ) {
        this.employees = new ArrayList<>();
    }

    public Manager(
        ArrayList<Employee> employees    ) {
        this.employees = employees;
    }


    public List<Employee> getEmployees() {
        return employees;
    }

    public void addEmployee(Employee employee) {
        this.employees.add(employee);
    }

}