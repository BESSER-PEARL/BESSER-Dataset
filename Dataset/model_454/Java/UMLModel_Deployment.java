





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Deployment extends Dependency {

    private String location;
    private String deployedArtifact;





    private UMLModel_DeploymentTarget umlmodel_deploymenttarget;


    public UMLModel_Deployment(
        String location,        String deployedArtifact    ) {
        super(
        );
        this.location = location;
        this.deployedArtifact = deployedArtifact;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getDeployedartifact() {
        return deployedArtifact;
    }

    public void setDeployedartifact(String deployedArtifact) {
        this.deployedArtifact = deployedArtifact;
    }

    public UMLModel_DeploymentTarget getUmlmodel_deploymenttarget() {
        return umlmodel_deploymenttarget;
    }

    public void setUmlmodel_deploymenttarget(UMLModel_DeploymentTarget umlmodel_deploymenttarget) {
        this.umlmodel_deploymenttarget = umlmodel_deploymenttarget;
    }

}