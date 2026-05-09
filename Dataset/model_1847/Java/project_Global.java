





import java.util.List;
import java.util.ArrayList;

public class project_Global  {






    private project_Project project_project;




    private List<project_Property> project_propertys;


    public project_Global(
    ) {
        this.project_propertys = new ArrayList<>();
    }

    public project_Global(
        ArrayList<project_Property> project_propertys    ) {
        this.project_propertys = project_propertys;
    }


    public project_Project getProject_project() {
        return project_project;
    }

    public void setProject_project(project_Project project_project) {
        this.project_project = project_project;
    }
    public List<project_Property> getProject_propertys() {
        return project_propertys;
    }

    public void addProject_property(Project_property project_property) {
        this.project_propertys.add(project_property);
    }

}