





import java.util.List;
import java.util.ArrayList;

public class PSM_MicroserviceProject extends ArtifactElement {

    private String ProjectArtifactId;





    private PSM_ApplicationProject psm_applicationproject;


    public PSM_MicroserviceProject(
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

    public PSM_ApplicationProject getPsm_applicationproject() {
        return psm_applicationproject;
    }

    public void setPsm_applicationproject(PSM_ApplicationProject psm_applicationproject) {
        this.psm_applicationproject = psm_applicationproject;
    }

}