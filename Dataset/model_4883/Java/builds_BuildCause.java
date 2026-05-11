





import java.util.List;
import java.util.ArrayList;

public class builds_BuildCause  {

    private String description;





    private builds_Build builds_build;




    private builds_User builds_user;


    public builds_BuildCause(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public builds_Build getBuilds_build() {
        return builds_build;
    }

    public void setBuilds_build(builds_Build builds_build) {
        this.builds_build = builds_build;
    }
    public builds_User getBuilds_user() {
        return builds_user;
    }

    public void setBuilds_user(builds_User builds_user) {
        this.builds_user = builds_user;
    }

}