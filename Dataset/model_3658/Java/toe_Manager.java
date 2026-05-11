





import java.util.List;
import java.util.ArrayList;

public class toe_Manager extends Employee {






    private List<toe_Project> toe_projects;




    private toe_Department toe_department;




    private toe_Project toe_project;




    private toe_Department toe_department;


    public toe_Manager(
    ) {
        super(
        );
        this.toe_projects = new ArrayList<>();
    }

    public toe_Manager(
        ArrayList<toe_Project> toe_projects    ) {
        this.toe_projects = toe_projects;
    }


    public List<toe_Project> getToe_projects() {
        return toe_projects;
    }

    public void addToe_project(Toe_project toe_project) {
        this.toe_projects.add(toe_project);
    }
    public toe_Department getToe_department() {
        return toe_department;
    }

    public void setToe_department(toe_Department toe_department) {
        this.toe_department = toe_department;
    }
    public toe_Project getToe_project() {
        return toe_project;
    }

    public void setToe_project(toe_Project toe_project) {
        this.toe_project = toe_project;
    }
    public toe_Department getToe_department() {
        return toe_department;
    }

    public void setToe_department(toe_Department toe_department) {
        this.toe_department = toe_department;
    }

}