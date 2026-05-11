





import java.util.List;
import java.util.ArrayList;

public class employee_Employee  {

    private String lastName;
    private String firstName;
    private String gender;
    private float salary;
    private String responsibilities;





    private List<employee_Employee> employee_employees;




    private List<employee_Project> employee_projects;




    private employee_Employee employee_employee;




    private employee_Project employee_project;




    private employee_Directory employee_directory;


    public employee_Employee(
        String lastName,        String firstName,        String gender,        float salary,        String responsibilities    ) {
        this.lastName = lastName;
        this.firstName = firstName;
        this.gender = gender;
        this.salary = salary;
        this.responsibilities = responsibilities;
        this.employee_employees = new ArrayList<>();
        this.employee_projects = new ArrayList<>();
    }

    public employee_Employee(
        String lastName,        String firstName,        String gender,        float salary,        String responsibilities        ArrayList<employee_Employee> employee_employees,        ArrayList<employee_Project> employee_projects    ) {
        this.lastName = lastName;
        this.firstName = firstName;
        this.gender = gender;
        this.salary = salary;
        this.responsibilities = responsibilities;
        this.employee_employees = employee_employees;
        this.employee_projects = employee_projects;
    }

    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }
    public String getResponsibilities() {
        return responsibilities;
    }

    public void setResponsibilities(String responsibilities) {
        this.responsibilities = responsibilities;
    }

    public List<employee_Employee> getEmployee_employees() {
        return employee_employees;
    }

    public void addEmployee_employee(Employee_employee employee_employee) {
        this.employee_employees.add(employee_employee);
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
    public employee_Project getEmployee_project() {
        return employee_project;
    }

    public void setEmployee_project(employee_Project employee_project) {
        this.employee_project = employee_project;
    }
    public employee_Directory getEmployee_directory() {
        return employee_directory;
    }

    public void setEmployee_directory(employee_Directory employee_directory) {
        this.employee_directory = employee_directory;
    }

}