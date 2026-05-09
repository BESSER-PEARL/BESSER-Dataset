





import java.util.List;
import java.util.ArrayList;

public class PSM_DockerContainerDefinition extends ArtifactElement {

    private String ContainerName;
    private String BuildField;
    private String ImageField;
    private boolean GeneratesLogs;





    private PSM_DistributedApplicationProject psm_distributedapplicationproject;


    public PSM_DockerContainerDefinition(
        String ContainerName,        String BuildField,        String ImageField,        boolean GeneratesLogs    ) {
        super(
        );
        this.ContainerName = ContainerName;
        this.BuildField = BuildField;
        this.ImageField = ImageField;
        this.GeneratesLogs = GeneratesLogs;
    }


    public String getContainername() {
        return ContainerName;
    }

    public void setContainername(String ContainerName) {
        this.ContainerName = ContainerName;
    }
    public String getBuildfield() {
        return BuildField;
    }

    public void setBuildfield(String BuildField) {
        this.BuildField = BuildField;
    }
    public String getImagefield() {
        return ImageField;
    }

    public void setImagefield(String ImageField) {
        this.ImageField = ImageField;
    }
    public boolean getGenerateslogs() {
        return GeneratesLogs;
    }

    public void setGenerateslogs(boolean GeneratesLogs) {
        this.GeneratesLogs = GeneratesLogs;
    }

    public PSM_DistributedApplicationProject getPsm_distributedapplicationproject() {
        return psm_distributedapplicationproject;
    }

    public void setPsm_distributedapplicationproject(PSM_DistributedApplicationProject psm_distributedapplicationproject) {
        this.psm_distributedapplicationproject = psm_distributedapplicationproject;
    }

}