





import java.util.List;
import java.util.ArrayList;

public class organizationchart_OrganizationalStructure  {

    private String type;
    private String name;





    private organizationchart_Employee organizationchart_employee;




    private organizationchart_Employee organizationchart_employee;




    private List<organizationchart_Employee> organizationchart_employees;




    private List<organizationchart_Function> organizationchart_functions;




    private organizationchart_Employee organizationchart_employee;




    private organizationchart_Organization organizationchart_organization;




    private List<organizationchart_OrganizationalStructure> organizationchart_organizationalstructures;


    public organizationchart_OrganizationalStructure(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
        this.organizationchart_employees = new ArrayList<>();
        this.organizationchart_functions = new ArrayList<>();
        this.organizationchart_organizationalstructures = new ArrayList<>();
    }

    public organizationchart_OrganizationalStructure(
        String type,        String name        ArrayList<organizationchart_Employee> organizationchart_employees,        ArrayList<organizationchart_Function> organizationchart_functions,        ArrayList<organizationchart_OrganizationalStructure> organizationchart_organizationalstructures    ) {
        this.type = type;
        this.name = name;
        this.organizationchart_employees = organizationchart_employees;
        this.organizationchart_functions = organizationchart_functions;
        this.organizationchart_organizationalstructures = organizationchart_organizationalstructures;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public organizationchart_Employee getOrganizationchart_employee() {
        return organizationchart_employee;
    }

    public void setOrganizationchart_employee(organizationchart_Employee organizationchart_employee) {
        this.organizationchart_employee = organizationchart_employee;
    }
    public organizationchart_Employee getOrganizationchart_employee() {
        return organizationchart_employee;
    }

    public void setOrganizationchart_employee(organizationchart_Employee organizationchart_employee) {
        this.organizationchart_employee = organizationchart_employee;
    }
    public List<organizationchart_Employee> getOrganizationchart_employees() {
        return organizationchart_employees;
    }

    public void addOrganizationchart_employee(Organizationchart_employee organizationchart_employee) {
        this.organizationchart_employees.add(organizationchart_employee);
    }
    public List<organizationchart_Function> getOrganizationchart_functions() {
        return organizationchart_functions;
    }

    public void addOrganizationchart_function(Organizationchart_function organizationchart_function) {
        this.organizationchart_functions.add(organizationchart_function);
    }
    public organizationchart_Employee getOrganizationchart_employee() {
        return organizationchart_employee;
    }

    public void setOrganizationchart_employee(organizationchart_Employee organizationchart_employee) {
        this.organizationchart_employee = organizationchart_employee;
    }
    public organizationchart_Organization getOrganizationchart_organization() {
        return organizationchart_organization;
    }

    public void setOrganizationchart_organization(organizationchart_Organization organizationchart_organization) {
        this.organizationchart_organization = organizationchart_organization;
    }
    public List<organizationchart_OrganizationalStructure> getOrganizationchart_organizationalstructures() {
        return organizationchart_organizationalstructures;
    }

    public void addOrganizationchart_organizationalstructure(Organizationchart_organizationalstructure organizationchart_organizationalstructure) {
        this.organizationchart_organizationalstructures.add(organizationchart_organizationalstructure);
    }

}