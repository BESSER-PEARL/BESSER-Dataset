





import java.util.List;
import java.util.ArrayList;

public class project_Managers extends ResourceAttribute {






    private List<project_Resource> project_resources;


    public project_Managers(
    ) {
        super(
        );
        this.project_resources = new ArrayList<>();
    }

    public project_Managers(
        ArrayList<project_Resource> project_resources    ) {
        this.project_resources = project_resources;
    }


    public List<project_Resource> getProject_resources() {
        return project_resources;
    }

    public void addProject_resource(Project_resource project_resource) {
        this.project_resources.add(project_resource);
    }

}