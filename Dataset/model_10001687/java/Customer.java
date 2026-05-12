





import java.util.List;
import java.util.ArrayList;

public class Customer  {






    private Online_Portal online_portal;




    private List<Employee> employees;




    private List<Manager> managers;




    private Store store;


    public Customer(
    ) {
        this.employees = new ArrayList<>();
        this.managers = new ArrayList<>();
    }

    public Customer(
        ArrayList<Employee> employees,        ArrayList<Manager> managers    ) {
        this.employees = employees;
        this.managers = managers;
    }


    public Online_Portal getOnline_portal() {
        return online_portal;
    }

    public void setOnline_portal(Online_Portal online_portal) {
        this.online_portal = online_portal;
    }
    public List<Employee> getEmployees() {
        return employees;
    }

    public void addEmployee(Employee employee) {
        this.employees.add(employee);
    }
    public List<Manager> getManagers() {
        return managers;
    }

    public void addManager(Manager manager) {
        this.managers.add(manager);
    }
    public Store getStore() {
        return store;
    }

    public void setStore(Store store) {
        this.store = store;
    }

}