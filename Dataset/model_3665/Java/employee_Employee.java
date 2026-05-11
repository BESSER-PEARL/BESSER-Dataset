





import java.util.List;
import java.util.ArrayList;

public class employee_Employee  {

    private String lastName;
    private float salary;
    private String version;
    private String responsibilities;
    private String gender;
    private String firstName;





    private employee_Project employee_project;




    private employee_Employee employee_employee;




    private List<employee_Project> employee_projects;




    private employee_Employee employee_employee;


    public employee_Employee(
        String lastName,        float salary,        String version,        String responsibilities,        String gender,        String firstName    ) {
        this.lastName = lastName;
        this.salary = salary;
        this.version = version;
        this.responsibilities = responsibilities;
        this.gender = gender;
        this.firstName = firstName;
        this.employee_projects = new ArrayList<>();
    }

    public employee_Employee(
        String lastName,        float salary,        String version,        String responsibilities,        String gender,        String firstName        ArrayList<employee_Project> employee_projects    ) {
        this.lastName = lastName;
        this.salary = salary;
        this.version = version;
        this.responsibilities = responsibilities;
        this.gender = gender;
        this.firstName = firstName;
        this.employee_projects = employee_projects;
    }

    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getResponsibilities() {
        return responsibilities;
    }

    public void setResponsibilities(String responsibilities) {
        this.responsibilities = responsibilities;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public employee_Project getEmployee_project() {
        return employee_project;
    }

    public void setEmployee_project(employee_Project employee_project) {
        this.employee_project = employee_project;
    }
    public employee_Employee getEmployee_employee() {
        return employee_employee;
    }

    public void setEmployee_employee(employee_Employee employee_employee) {
        this.employee_employee = employee_employee;
    }
    public List<employee_Project> getEmployee_projects() {
        return employee_projects;
    }

    public void addEmployee_project(Employee_project employee_project) {
        this.employee_projects.add(employee_project);
    }
    public employee_Employee getEmployee_employee() {
        return employee_employee;
    }

    public void setEmployee_employee(employee_Employee employee_employee) {
        this.employee_employee = employee_employee;
    }

}