





import java.util.List;
import java.util.ArrayList;

public class uml_Deployment extends Dependency {






    private uml_DeploymentTarget uml_deploymenttarget;




    private List<uml_DeployedArtifact> uml_deployedartifacts;




    private uml_DeploymentTarget uml_deploymenttarget;


    public uml_Deployment(
    ) {
        super(
        );
        this.uml_deployedartifacts = new ArrayList<>();
    }

    public uml_Deployment(
        ArrayList<uml_DeployedArtifact> uml_deployedartifacts    ) {
        this.uml_deployedartifacts = uml_deployedartifacts;
    }


    public uml_DeploymentTarget getUml_deploymenttarget() {
        return uml_deploymenttarget;
    }

    public void setUml_deploymenttarget(uml_DeploymentTarget uml_deploymenttarget) {
        this.uml_deploymenttarget = uml_deploymenttarget;
    }
    public List<uml_DeployedArtifact> getUml_deployedartifacts() {
        return uml_deployedartifacts;
    }

    public void addUml_deployedartifact(Uml_deployedartifact uml_deployedartifact) {
        this.uml_deployedartifacts.add(uml_deployedartifact);
    }
    public uml_DeploymentTarget getUml_deploymenttarget() {
        return uml_deploymenttarget;
    }

    public void setUml_deploymenttarget(uml_DeploymentTarget uml_deploymenttarget) {
        this.uml_deploymenttarget = uml_deploymenttarget;
    }

}