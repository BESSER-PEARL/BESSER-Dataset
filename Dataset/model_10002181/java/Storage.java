





import java.util.List;
import java.util.ArrayList;

public class Storage  {

    private int Component_id;
    private String Component_Name;





    private List<Employee> employees;


    public Storage(
        int Component_id,        String Component_Name    ) {
        this.Component_id = Component_id;
        this.Component_Name = Component_Name;
        this.employees = new ArrayList<>();
    }

    public Storage(
        int Component_id,        String Component_Name        ArrayList<Employee> employees    ) {
        this.Component_id = Component_id;
        this.Component_Name = Component_Name;
        this.employees = employees;
    }

    public int getComponent_id() {
        return Component_id;
    }

    public void setComponent_id(int Component_id) {
        this.Component_id = Component_id;
    }
    public String getComponent_name() {
        return Component_Name;
    }

    public void setComponent_name(String Component_Name) {
        this.Component_Name = Component_Name;
    }

    public List<Employee> getEmployees() {
        return employees;
    }

    public void addEmployee(Employee employee) {
        this.employees.add(employee);
    }

}