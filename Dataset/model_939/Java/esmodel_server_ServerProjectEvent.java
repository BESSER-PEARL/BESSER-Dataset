





import java.util.List;
import java.util.ArrayList;

public class esmodel_server_ServerProjectEvent extends ServerEvent {






    private ProjectId projectid;


    public esmodel_server_ServerProjectEvent(
    ) {
        super(
        );
    }



    public ProjectId getProjectid() {
        return projectid;
    }

    public void setProjectid(ProjectId projectid) {
        this.projectid = projectid;
    }

}