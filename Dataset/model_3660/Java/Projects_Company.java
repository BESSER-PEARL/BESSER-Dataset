





import java.util.List;
import java.util.ArrayList;

public class Projects_Company  {

    private String name;





    private List<Projects_Project> projects_projects;




    private Projects_Project projects_project;




    private Projects_Worker projects_worker;




    private List<Projects_Worker> projects_workers;


    public Projects_Company(
        String name    ) {
        this.name = name;
        this.projects_projects = new ArrayList<>();
        this.projects_workers = new ArrayList<>();
    }

    public Projects_Company(
        String name        ArrayList<Projects_Project> projects_projects,        ArrayList<Projects_Worker> projects_workers    ) {
        this.name = name;
        this.projects_projects = projects_projects;
        this.projects_workers = projects_workers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Projects_Project> getProjects_projects() {
        return projects_projects;
    }

    public void addProjects_project(Projects_project projects_project) {
        this.projects_projects.add(projects_project);
    }
    public Projects_Project getProjects_project() {
        return projects_project;
    }

    public void setProjects_project(Projects_Project projects_project) {
        this.projects_project = projects_project;
    }
    public Projects_Worker getProjects_worker() {
        return projects_worker;
    }

    public void setProjects_worker(Projects_Worker projects_worker) {
        this.projects_worker = projects_worker;
    }
    public List<Projects_Worker> getProjects_workers() {
        return projects_workers;
    }

    public void addProjects_worker(Projects_worker projects_worker) {
        this.projects_workers.add(projects_worker);
    }

}