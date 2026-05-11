





import java.util.List;
import java.util.ArrayList;

public class Project_Department  {

    private String name;
    private int budget;
    private String location;





    private Project_Employee project_employee;




    private List<Project_Employee> project_employees;


    public Project_Department(
        String name,        int budget,        String location    ) {
        this.name = name;
        this.budget = budget;
        this.location = location;
        this.project_employees = new ArrayList<>();
    }

    public Project_Department(
        String name,        int budget,        String location        ArrayList<Project_Employee> project_employees    ) {
        this.name = name;
        this.budget = budget;
        this.location = location;
        this.project_employees = project_employees;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getBudget() {
        return budget;
    }

    public void setBudget(int budget) {
        this.budget = budget;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public Project_Employee getProject_employee() {
        return project_employee;
    }

    public void setProject_employee(Project_Employee project_employee) {
        this.project_employee = project_employee;
    }
    public List<Project_Employee> getProject_employees() {
        return project_employees;
    }

    public void addProject_employee(Project_employee project_employee) {
        this.project_employees.add(project_employee);
    }

}