





import java.util.List;
import java.util.ArrayList;

public class esmodel_roles_Role  {






    private List<ProjectId> projectids;


    public esmodel_roles_Role(
    ) {
        this.projectids = new ArrayList<>();
    }

    public esmodel_roles_Role(
        ArrayList<ProjectId> projectids    ) {
        this.projectids = projectids;
    }


    public List<ProjectId> getProjectids() {
        return projectids;
    }

    public void addProjectid(Projectid projectid) {
        this.projectids.add(projectid);
    }

}