





import java.util.List;
import java.util.ArrayList;

public class esmodel_ProjectInfo  {

    private String description;
    private String name;





    private ProjectId projectid;


    public esmodel_ProjectInfo(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ProjectId getProjectid() {
        return projectid;
    }

    public void setProjectid(ProjectId projectid) {
        this.projectid = projectid;
    }

}