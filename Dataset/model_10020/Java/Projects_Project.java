





import java.util.List;
import java.util.ArrayList;

public class Projects_Project  {

    private String status;
    private String name;
    private String size;





    private Projects_Worker projects_worker;




    private Projects_Project projects_project;




    private Projects_Qualification projects_qualification;




    private List<Projects_Worker> projects_workers;




    private Projects_Company projects_company;




    private Projects_Company projects_company;




    private List<Projects_Qualification> projects_qualifications;




    private Projects_Project projects_project;


    public Projects_Project(
        String status,        String name,        String size    ) {
        this.status = status;
        this.name = name;
        this.size = size;
        this.projects_workers = new ArrayList<>();
        this.projects_qualifications = new ArrayList<>();
    }

    public Projects_Project(
        String status,        String name,        String size        ArrayList<Projects_Worker> projects_workers,        ArrayList<Projects_Qualification> projects_qualifications    ) {
        this.status = status;
        this.name = name;
        this.size = size;
        this.projects_workers = projects_workers;
        this.projects_qualifications = projects_qualifications;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public Projects_Worker getProjects_worker() {
        return projects_worker;
    }

    public void setProjects_worker(Projects_Worker projects_worker) {
        this.projects_worker = projects_worker;
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
    public List<Projects_Worker> getProjects_workers() {
        return projects_workers;
    }

    public void addProjects_worker(Projects_worker projects_worker) {
        this.projects_workers.add(projects_worker);
    }
    public Projects_Company getProjects_company() {
        return projects_company;
    }

    public void setProjects_company(Projects_Company projects_company) {
        this.projects_company = projects_company;
    }
    public Projects_Company getProjects_company() {
        return projects_company;
    }

    public void setProjects_company(Projects_Company projects_company) {
        this.projects_company = projects_company;
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

}