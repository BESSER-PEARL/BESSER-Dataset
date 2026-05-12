





import java.util.List;
import java.util.ArrayList;

public class SWRC_Organization  {

    private String name;
    private String location;





    private List<Project> projects;




    private List<Project> projects;




    private List<Publication> publications;




    private List<Employee> employees;


    public SWRC_Organization(
        String name,        String location    ) {
        this.name = name;
        this.location = location;
        this.projects = new ArrayList<>();
        this.projects = new ArrayList<>();
        this.publications = new ArrayList<>();
        this.employees = new ArrayList<>();
    }

    public SWRC_Organization(
        String name,        String location        ArrayList<Project> projects,        ArrayList<Project> projects,        ArrayList<Publication> publications,        ArrayList<Employee> employees    ) {
        this.name = name;
        this.location = location;
        this.projects = projects;
        this.projects = projects;
        this.publications = publications;
        this.employees = employees;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public List<Project> getProjects() {
        return projects;
    }

    public void addProject(Project project) {
        this.projects.add(project);
    }
    public List<Project> getProjects() {
        return projects;
    }

    public void addProject(Project project) {
        this.projects.add(project);
    }
    public List<Publication> getPublications() {
        return publications;
    }

    public void addPublication(Publication publication) {
        this.publications.add(publication);
    }
    public List<Employee> getEmployees() {
        return employees;
    }

    public void addEmployee(Employee employee) {
        this.employees.add(employee);
    }

}