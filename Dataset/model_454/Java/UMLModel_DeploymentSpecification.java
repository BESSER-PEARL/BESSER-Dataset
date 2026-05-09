





import java.util.List;
import java.util.ArrayList;

public class UMLModel_DeploymentSpecification extends Artifact {

    private String deployment;
    private String deploymentLocation;
    private String executionLocation;





    private UMLModel_Deployment umlmodel_deployment;


    public UMLModel_DeploymentSpecification(
        String deployment,        String deploymentLocation,        String executionLocation    ) {
        super(
        );
        this.deployment = deployment;
        this.deploymentLocation = deploymentLocation;
        this.executionLocation = executionLocation;
    }


    public String getDeployment() {
        return deployment;
    }

    public void setDeployment(String deployment) {
        this.deployment = deployment;
    }
    public String getDeploymentlocation() {
        return deploymentLocation;
    }

    public void setDeploymentlocation(String deploymentLocation) {
        this.deploymentLocation = deploymentLocation;
    }
    public String getExecutionlocation() {
        return executionLocation;
    }

    public void setExecutionlocation(String executionLocation) {
        this.executionLocation = executionLocation;
    }

    public UMLModel_Deployment getUmlmodel_deployment() {
        return umlmodel_deployment;
    }

    public void setUmlmodel_deployment(UMLModel_Deployment umlmodel_deployment) {
        this.umlmodel_deployment = umlmodel_deployment;
    }

}