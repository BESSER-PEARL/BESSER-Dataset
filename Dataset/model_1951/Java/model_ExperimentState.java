





import java.util.List;
import java.util.ArrayList;

public class model_ExperimentState  {

    private String projectId;
    private String experimentId;



    public model_ExperimentState(
        String projectId,        String experimentId    ) {
        this.projectId = projectId;
        this.experimentId = experimentId;
    }


    public String getProjectid() {
        return projectId;
    }

    public void setProjectid(String projectId) {
        this.projectId = projectId;
    }
    public String getExperimentid() {
        return experimentId;
    }

    public void setExperimentid(String experimentId) {
        this.experimentId = experimentId;
    }


}