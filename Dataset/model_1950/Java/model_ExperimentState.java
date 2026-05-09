





import java.util.List;
import java.util.ArrayList;

public class model_ExperimentState  {

    private String experimentId;
    private String projectId;



    public model_ExperimentState(
        String experimentId,        String projectId    ) {
        this.experimentId = experimentId;
        this.projectId = projectId;
    }


    public String getExperimentid() {
        return experimentId;
    }

    public void setExperimentid(String experimentId) {
        this.experimentId = experimentId;
    }
    public String getProjectid() {
        return projectId;
    }

    public void setProjectid(String projectId) {
        this.projectId = projectId;
    }


}