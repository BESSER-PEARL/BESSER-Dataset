





import java.util.List;
import java.util.ArrayList;

public class Projects_Project  {

    private String name;
    private String status;
    private String size;





    private Projects_Project projects_project;




    private List<Projects_Qualification> projects_qualifications;




    private Projects_Project projects_project;




    private Projects_Qualification projects_qualification;


    public Projects_Project(
        String name,        String status,        String size    ) {
        this.name = name;
        this.status = status;
        this.size = size;
        this.projects_qualifications = new ArrayList<>();
    }

    public Projects_Project(
        String name,        String status,        String size        ArrayList<Projects_Qualification> projects_qualifications    ) {
        this.name = name;
        this.status = status;
        this.size = size;
        this.projects_qualifications = projects_qualifications;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public Projects_Project getProjects_project() {
        return projects_project;
    }

    public void setProjects_project(Projects_Project projects_project) {
        this.projects_project = projects_project;
    }
    public List<Projects_Qualification> getProjects_qualifications() {
        return projects_qualifications;
    }

    public void addProjects_qualification(Projects_qualification projects_qualification) {
        this.projects_qualifications.add(projects_qualification);
    }
    public Projects_Project getProjects_project() {
        return projects_project;
    }

    public void setProjects_project(Projects_Project projects_project) {
        this.projects_project = projects_project;
    }
    public Projects_Qualification getProjects_qualification() {
        return projects_qualification;
    }

    public void setProjects_qualification(Projects_Qualification projects_qualification) {
        this.projects_qualification = projects_qualification;
    }

}