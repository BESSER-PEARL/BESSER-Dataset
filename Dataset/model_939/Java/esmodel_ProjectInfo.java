





import java.util.List;
import java.util.ArrayList;

public class esmodel_ProjectInfo  {

    private String name;
    private String description;





    private ProjectId projectid;


    public esmodel_ProjectInfo(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public ProjectId getProjectid() {
        return projectid;
    }

    public void setProjectid(ProjectId projectid) {
        this.projectid = projectid;
    }

}