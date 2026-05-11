





import java.util.List;
import java.util.ArrayList;

public class ce_Company  {

    private String name;





    private List<ce_Employee> ce_employees;


    public ce_Company(
        String name    ) {
        this.name = name;
        this.ce_employees = new ArrayList<>();
    }

    public ce_Company(
        String name        ArrayList<ce_Employee> ce_employees    ) {
        this.name = name;
        this.ce_employees = ce_employees;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ce_Employee> getCe_employees() {
        return ce_employees;
    }

    public void addCe_employee(Ce_employee ce_employee) {
        this.ce_employees.add(ce_employee);
    }

}