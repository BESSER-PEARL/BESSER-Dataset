





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_DeploymentSpecification extends Artifact {

    private String deploymentLocation;
    private String executionLocation;





    private uml3_0_0_Deployment uml3_0_0_deployment;




    private uml3_0_0_Deployment uml3_0_0_deployment;


    public uml3_0_0_DeploymentSpecification(
        String deploymentLocation,        String executionLocation    ) {
        super(
        );
        this.deploymentLocation = deploymentLocation;
        this.executionLocation = executionLocation;
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

    public uml3_0_0_Deployment getUml3_0_0_deployment() {
        return uml3_0_0_deployment;
    }

    public void setUml3_0_0_deployment(uml3_0_0_Deployment uml3_0_0_deployment) {
        this.uml3_0_0_deployment = uml3_0_0_deployment;
    }
    public uml3_0_0_Deployment getUml3_0_0_deployment() {
        return uml3_0_0_deployment;
    }

    public void setUml3_0_0_deployment(uml3_0_0_Deployment uml3_0_0_deployment) {
        this.uml3_0_0_deployment = uml3_0_0_deployment;
    }

}