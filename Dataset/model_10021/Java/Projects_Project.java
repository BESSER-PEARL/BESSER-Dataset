





import java.util.List;
import java.util.ArrayList;

public class Projects_Project  {

    private String size;
    private String status;





    private Projects_Company projects_company;




    private List<Projects_Project> projects_projects;




    private Projects_Company projects_company;


    public Projects_Project(
        String size,        String status    ) {
        this.size = size;
        this.status = status;
        this.projects_projects = new ArrayList<>();
    }

    public Projects_Project(
        String size,        String status        ArrayList<Projects_Project> projects_projects    ) {
        this.size = size;
        this.status = status;
        this.projects_projects = projects_projects;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
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
    public Projects_Company getProjects_company() {
        return projects_company;
    }

    public void setProjects_company(Projects_Company projects_company) {
        this.projects_company = projects_company;
    }

}