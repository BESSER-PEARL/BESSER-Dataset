





import java.util.List;
import java.util.ArrayList;

public class cde_Department  {

    private String name;





    private cde_Company cde_company;




    private List<cde_Employee> cde_employees;


    public cde_Department(
        String name    ) {
        this.name = name;
        this.cde_employees = new ArrayList<>();
    }

    public cde_Department(
        String name        ArrayList<cde_Employee> cde_employees    ) {
        this.name = name;
        this.cde_employees = cde_employees;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cde_Company getCde_company() {
        return cde_company;
    }

    public void setCde_company(cde_Company cde_company) {
        this.cde_company = cde_company;
    }
    public List<cde_Employee> getCde_employees() {
        return cde_employees;
    }

    public void addCde_employee(Cde_employee cde_employee) {
        this.cde_employees.add(cde_employee);
    }

}