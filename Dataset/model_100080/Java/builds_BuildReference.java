





import java.util.List;
import java.util.ArrayList;

public class builds_BuildReference  {

    private String plan;
    private String build;





    private builds_BuildCause builds_buildcause;


    public builds_BuildReference(
        String plan,        String build    ) {
        this.plan = plan;
        this.build = build;
    }


    public String getPlan() {
        return plan;
    }

    public void setPlan(String plan) {
        this.plan = plan;
    }
    public String getBuild() {
        return build;
    }

    public void setBuild(String build) {
        this.build = build;
    }

    public builds_BuildCause getBuilds_buildcause() {
        return builds_buildcause;
    }

    public void setBuilds_buildcause(builds_BuildCause builds_buildcause) {
        this.builds_buildcause = builds_buildcause;
    }

}