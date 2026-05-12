





import java.util.List;
import java.util.ArrayList;

public class Projects_Worker  {






    private Projects_Company projects_company;




    private List<Projects_Project> projects_projects;




    private Projects_Project projects_project;


    public Projects_Worker(
    ) {
        this.projects_projects = new ArrayList<>();
    }

    public Projects_Worker(
        ArrayList<Projects_Project> projects_projects    ) {
        this.projects_projects = projects_projects;
    }


    public Projects_Company getProjects_company() {
        return projects_company;
    }

    public void setProjects_company(Projects_Company projects_company) {
        this.projects_company = projects_company;
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

}