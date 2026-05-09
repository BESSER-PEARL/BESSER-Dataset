





import java.util.List;
import java.util.ArrayList;

public class PSM_ApplicationProject extends ArtifactElement {

    private String ProjectArtifactId;





    private PSM_DistributedApplicationProject psm_distributedapplicationproject;


    public PSM_ApplicationProject(
        String ProjectArtifactId    ) {
        super(
        );
        this.ProjectArtifactId = ProjectArtifactId;
    }


    public String getProjectartifactid() {
        return ProjectArtifactId;
    }

    public void setProjectartifactid(String ProjectArtifactId) {
        this.ProjectArtifactId = ProjectArtifactId;
    }

    public PSM_DistributedApplicationProject getPsm_distributedapplicationproject() {
        return psm_distributedapplicationproject;
    }

    public void setPsm_distributedapplicationproject(PSM_DistributedApplicationProject psm_distributedapplicationproject) {
        this.psm_distributedapplicationproject = psm_distributedapplicationproject;
    }

}