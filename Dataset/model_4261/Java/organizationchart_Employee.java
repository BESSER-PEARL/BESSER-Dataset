





import java.util.List;
import java.util.ArrayList;

public class organizationchart_Employee  {

    private String lastname;
    private String firstname;
    private String title;
    private String trigraph;





    private organizationchart_Employee organizationchart_employee;




    private List<organizationchart_Function> organizationchart_functions;




    private organizationchart_Organization organizationchart_organization;




    private organizationchart_Employee organizationchart_employee;




    private organizationchart_Function organizationchart_function;


    public organizationchart_Employee(
        String lastname,        String firstname,        String title,        String trigraph    ) {
        this.lastname = lastname;
        this.firstname = firstname;
        this.title = title;
        this.trigraph = trigraph;
        this.organizationchart_functions = new ArrayList<>();
    }

    public organizationchart_Employee(
        String lastname,        String firstname,        String title,        String trigraph        ArrayList<organizationchart_Function> organizationchart_functions    ) {
        this.lastname = lastname;
        this.firstname = firstname;
        this.title = title;
        this.trigraph = trigraph;
        this.organizationchart_functions = organizationchart_functions;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getTrigraph() {
        return trigraph;
    }

    public void setTrigraph(String trigraph) {
        this.trigraph = trigraph;
    }

    public organizationchart_Employee getOrganizationchart_employee() {
        return organizationchart_employee;
    }

    public void setOrganizationchart_employee(organizationchart_Employee organizationchart_employee) {
        this.organizationchart_employee = organizationchart_employee;
    }
    public List<organizationchart_Function> getOrganizationchart_functions() {
        return organizationchart_functions;
    }

    public void addOrganizationchart_function(Organizationchart_function organizationchart_function) {
        this.organizationchart_functions.add(organizationchart_function);
    }
    public organizationchart_Organization getOrganizationchart_organization() {
        return organizationchart_organization;
    }

    public void setOrganizationchart_organization(organizationchart_Organization organizationchart_organization) {
        this.organizationchart_organization = organizationchart_organization;
    }
    public organizationchart_Employee getOrganizationchart_employee() {
        return organizationchart_employee;
    }

    public void setOrganizationchart_employee(organizationchart_Employee organizationchart_employee) {
        this.organizationchart_employee = organizationchart_employee;
    }
    public organizationchart_Function getOrganizationchart_function() {
        return organizationchart_function;
    }

    public void setOrganizationchart_function(organizationchart_Function organizationchart_function) {
        this.organizationchart_function = organizationchart_function;
    }

}