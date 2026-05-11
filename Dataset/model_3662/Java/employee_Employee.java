





import java.util.List;
import java.util.ArrayList;

public class employee_Employee  {

    private String firstName;
    private String id;
    private String gender;
    private String lastName;
    private String responsibilities;
    private float salary;





    private employee_Organization employee_organization;




    private employee_Employee employee_employee;




    private employee_Employee employee_employee;


    public employee_Employee(
        String firstName,        String id,        String gender,        String lastName,        String responsibilities,        float salary    ) {
        this.firstName = firstName;
        this.id = id;
        this.gender = gender;
        this.lastName = lastName;
        this.responsibilities = responsibilities;
        this.salary = salary;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getResponsibilities() {
        return responsibilities;
    }

    public void setResponsibilities(String responsibilities) {
        this.responsibilities = responsibilities;
    }
    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }

    public employee_Organization getEmployee_organization() {
        return employee_organization;
    }

    public void setEmployee_organization(employee_Organization employee_organization) {
        this.employee_organization = employee_organization;
    }
    public employee_Employee getEmployee_employee() {
        return employee_employee;
    }

    public void setEmployee_employee(employee_Employee employee_employee) {
        this.employee_employee = employee_employee;
    }
    public employee_Employee getEmployee_employee() {
        return employee_employee;
    }

    public void setEmployee_employee(employee_Employee employee_employee) {
        this.employee_employee = employee_employee;
    }

}