





import java.util.List;
import java.util.ArrayList;

public class UML2_DeploymentSpecification extends Artifact {

    private String executionLocation;
    private String deploymentLocation;





    private UML2_Deployment uml2_deployment;


    public UML2_DeploymentSpecification(
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

    public UML2_Deployment getUml2_deployment() {
        return uml2_deployment;
    }

    public void setUml2_deployment(UML2_Deployment uml2_deployment) {
        this.uml2_deployment = uml2_deployment;
    }

}