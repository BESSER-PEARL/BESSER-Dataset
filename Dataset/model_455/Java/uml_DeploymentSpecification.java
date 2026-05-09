





import java.util.List;
import java.util.ArrayList;

public class uml_DeploymentSpecification extends Artifact {

    private String executionLocation;
    private String deploymentLocation;





    private uml_Deployment uml_deployment;




    private uml_Deployment uml_deployment;


    public uml_DeploymentSpecification(
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

    public uml_Deployment getUml_deployment() {
        return uml_deployment;
    }

    public void setUml_deployment(uml_Deployment uml_deployment) {
        this.uml_deployment = uml_deployment;
    }
    public uml_Deployment getUml_deployment() {
        return uml_deployment;
    }

    public void setUml_deployment(uml_Deployment uml_deployment) {
        this.uml_deployment = uml_deployment;
    }

}