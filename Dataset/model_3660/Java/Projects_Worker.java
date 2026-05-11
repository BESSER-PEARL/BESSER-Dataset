





import java.util.List;
import java.util.ArrayList;

public class Projects_Worker  {

    private String nickname;
    private int salary;





    private List<Projects_Qualification> projects_qualifications;




    private List<Projects_Project> projects_projects;




    private Projects_Project projects_project;




    private Projects_Qualification projects_qualification;


    public Projects_Worker(
        String nickname,        int salary    ) {
        this.nickname = nickname;
        this.salary = salary;
        this.projects_qualifications = new ArrayList<>();
        this.projects_projects = new ArrayList<>();
    }

    public Projects_Worker(
        String nickname,        int salary        ArrayList<Projects_Qualification> projects_qualifications,        ArrayList<Projects_Project> projects_projects    ) {
        this.nickname = nickname;
        this.salary = salary;
        this.projects_qualifications = projects_qualifications;
        this.projects_projects = projects_projects;
    }

    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }
    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    public List<Projects_Qualification> getProjects_qualifications() {
        return projects_qualifications;
    }

    public void addProjects_qualification(Projects_qualification projects_qualification) {
        this.projects_qualifications.add(projects_qualification);
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
    public Projects_Qualification getProjects_qualification() {
        return projects_qualification;
    }

    public void setProjects_qualification(Projects_Qualification projects_qualification) {
        this.projects_qualification = projects_qualification;
    }

}