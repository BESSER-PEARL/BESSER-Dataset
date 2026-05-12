





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String Name;
    private String Email;





    private List<Employee> employees;


    public Admin(
        String Name,        String Email    ) {
        this.Name = Name;
        this.Email = Email;
        this.employees = new ArrayList<>();
    }

    public Admin(
        String Name,        String Email        ArrayList<Employee> employees    ) {
        this.Name = Name;
        this.Email = Email;
        this.employees = employees;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }

    public List<Employee> getEmployees() {
        return employees;
    }

    public void addEmployee(Employee employee) {
        this.employees.add(employee);
    }

}