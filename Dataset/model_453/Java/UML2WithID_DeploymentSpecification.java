





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_DeploymentSpecification extends Artifact {

    private String executionLocation;
    private String deploymentLocation;





    private UML2WithID_Deployment uml2withid_deployment;


    public UML2WithID_DeploymentSpecification(
        String executionLocation,        String deploymentLocation    ) {
        super(
        );
        this.executionLocation = executionLocation;
        this.deploymentLocation = deploymentLocation;
    }


    public String getExecutionlocation() {
        return executionLocation;
    }

    public void setExecutionlocation(String executionLocation) {
        this.executionLocation = executionLocation;
    }
    public String getDeploymentlocation() {
        return deploymentLocation;
    }

    public void setDeploymentlocation(String deploymentLocation) {
        this.deploymentLocation = deploymentLocation;
    }

    public UML2WithID_Deployment getUml2withid_deployment() {
        return uml2withid_deployment;
    }

    public void setUml2withid_deployment(UML2WithID_Deployment uml2withid_deployment) {
        this.uml2withid_deployment = uml2withid_deployment;
    }

}