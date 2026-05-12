





import java.util.List;
import java.util.ArrayList;

public class Projects_Qualification  {

    private String description;





    private Projects_Worker projects_worker;




    private List<Projects_Worker> projects_workers;


    public Projects_Qualification(
        String description    ) {
        this.description = description;
        this.projects_workers = new ArrayList<>();
    }

    public Projects_Qualification(
        String description        ArrayList<Projects_Worker> projects_workers    ) {
        this.description = description;
        this.projects_workers = projects_workers;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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