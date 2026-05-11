





import java.util.List;
import java.util.ArrayList;

public class organizationchart_Location  {

    private String name;





    private organizationchart_Organization organizationchart_organization;




    private List<organizationchart_Employee> organizationchart_employees;




    private organizationchart_Employee organizationchart_employee;


    public organizationchart_Location(
        String name    ) {
        this.name = name;
        this.organizationchart_employees = new ArrayList<>();
    }

    public organizationchart_Location(
        String name        ArrayList<organizationchart_Employee> organizationchart_employees    ) {
        this.name = name;
        this.organizationchart_employees = organizationchart_employees;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public organizationchart_Organization getOrganizationchart_organization() {
        return organizationchart_organization;
    }

    public void setOrganizationchart_organization(organizationchart_Organization organizationchart_organization) {
        this.organizationchart_organization = organizationchart_organization;
    }
    public List<organizationchart_Employee> getOrganizationchart_employees() {
        return organizationchart_employees;
    }

    public void addOrganizationchart_employee(Organizationchart_employee organizationchart_employee) {
        this.organizationchart_employees.add(organizationchart_employee);
    }
    public organizationchart_Employee getOrganizationchart_employee() {
        return organizationchart_employee;
    }

    public void setOrganizationchart_employee(organizationchart_Employee organizationchart_employee) {
        this.organizationchart_employee = organizationchart_employee;
    }

}