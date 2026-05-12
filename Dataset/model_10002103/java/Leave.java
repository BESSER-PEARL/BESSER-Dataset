





import java.util.List;
import java.util.ArrayList;

public class Leave  {

    private int l_emp_id;
    private String l_type;
    private String l_description;
    private int l_id;





    private Admin admin;




    private List<Employee> employees;


    public Leave(
        int l_emp_id,        String l_type,        String l_description,        int l_id    ) {
        this.l_emp_id = l_emp_id;
        this.l_type = l_type;
        this.l_description = l_description;
        this.l_id = l_id;
        this.employees = new ArrayList<>();
    }

    public Leave(
        int l_emp_id,        String l_type,        String l_description,        int l_id        ArrayList<Employee> employees    ) {
        this.l_emp_id = l_emp_id;
        this.l_type = l_type;
        this.l_description = l_description;
        this.l_id = l_id;
        this.employees = employees;
    }

    public int getL_emp_id() {
        return l_emp_id;
    }

    public void setL_emp_id(int l_emp_id) {
        this.l_emp_id = l_emp_id;
    }
    public String getL_type() {
        return l_type;
    }

    public void setL_type(String l_type) {
        this.l_type = l_type;
    }
    public String getL_description() {
        return l_description;
    }

    public void setL_description(String l_description) {
        this.l_description = l_description;
    }
    public int getL_id() {
        return l_id;
    }

    public void setL_id(int l_id) {
        this.l_id = l_id;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public List<Employee> getEmployees() {
        return employees;
    }

    public void addEmployee(Employee employee) {
        this.employees.add(employee);
    }

}