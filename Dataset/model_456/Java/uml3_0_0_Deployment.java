





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Deployment extends Dependency {






    private uml3_0_0_DeploymentTarget uml3_0_0_deploymenttarget;




    private List<uml3_0_0_DeployedArtifact> uml3_0_0_deployedartifacts;




    private uml3_0_0_DeploymentTarget uml3_0_0_deploymenttarget;


    public uml3_0_0_Deployment(
    ) {
        super(
        );
        this.uml3_0_0_deployedartifacts = new ArrayList<>();
    }

    public uml3_0_0_Deployment(
        ArrayList<uml3_0_0_DeployedArtifact> uml3_0_0_deployedartifacts    ) {
        this.uml3_0_0_deployedartifacts = uml3_0_0_deployedartifacts;
    }


    public uml3_0_0_DeploymentTarget getUml3_0_0_deploymenttarget() {
        return uml3_0_0_deploymenttarget;
    }

    public void setUml3_0_0_deploymenttarget(uml3_0_0_DeploymentTarget uml3_0_0_deploymenttarget) {
        this.uml3_0_0_deploymenttarget = uml3_0_0_deploymenttarget;
    }
    public List<uml3_0_0_DeployedArtifact> getUml3_0_0_deployedartifacts() {
        return uml3_0_0_deployedartifacts;
    }

    public void addUml3_0_0_deployedartifact(Uml3_0_0_deployedartifact uml3_0_0_deployedartifact) {
        this.uml3_0_0_deployedartifacts.add(uml3_0_0_deployedartifact);
    }
    public uml3_0_0_DeploymentTarget getUml3_0_0_deploymenttarget() {
        return uml3_0_0_deploymenttarget;
    }

    public void setUml3_0_0_deploymenttarget(uml3_0_0_DeploymentTarget uml3_0_0_deploymenttarget) {
        this.uml3_0_0_deploymenttarget = uml3_0_0_deploymenttarget;
    }

}