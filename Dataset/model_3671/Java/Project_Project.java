





import java.util.List;
import java.util.ArrayList;

public class Project_Project  {

    private int budget;
    private String name;





    private Project_Employee project_employee;




    private Project_Department project_department;




    private List<Project_Employee> project_employees;




    private Project_Department project_department;


    public Project_Project(
        int budget,        String name    ) {
        this.budget = budget;
        this.name = name;
        this.project_employees = new ArrayList<>();
    }

    public Project_Project(
        int budget,        String name        ArrayList<Project_Employee> project_employees    ) {
        this.budget = budget;
        this.name = name;
        this.project_employees = project_employees;
    }

    public int getBudget() {
        return budget;
    }

    public void setBudget(int budget) {
        this.budget = budget;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Project_Employee getProject_employee() {
        return project_employee;
    }

    public void setProject_employee(Project_Employee project_employee) {
        this.project_employee = project_employee;
    }
    public Project_Department getProject_department() {
        return project_department;
    }

    public void setProject_department(Project_Department project_department) {
        this.project_department = project_department;
    }
    public List<Project_Employee> getProject_employees() {
        return project_employees;
    }

    public void addProject_employee(Project_employee project_employee) {
        this.project_employees.add(project_employee);
    }
    public Project_Department getProject_department() {
        return project_department;
    }

    public void setProject_department(Project_Department project_department) {
        this.project_department = project_department;
    }

}