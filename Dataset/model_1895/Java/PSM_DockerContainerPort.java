





import java.util.List;
import java.util.ArrayList;

public class PSM_DockerContainerPort extends ArtifactElement {

    private String ExposesPortsField;





    private PSM_DockerContainerDefinition psm_dockercontainerdefinition;


    public PSM_DockerContainerPort(
        String ExposesPortsField    ) {
        super(
        );
        this.ExposesPortsField = ExposesPortsField;
    }


    public String getExposesportsfield() {
        return ExposesPortsField;
    }

    public void setExposesportsfield(String ExposesPortsField) {
        this.ExposesPortsField = ExposesPortsField;
    }

    public PSM_DockerContainerDefinition getPsm_dockercontainerdefinition() {
        return psm_dockercontainerdefinition;
    }

    public void setPsm_dockercontainerdefinition(PSM_DockerContainerDefinition psm_dockercontainerdefinition) {
        this.psm_dockercontainerdefinition = psm_dockercontainerdefinition;
    }

}