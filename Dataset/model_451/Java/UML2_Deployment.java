





import java.util.List;
import java.util.ArrayList;

public class UML2_Deployment extends Dependency {






    private List<UML2_DeployedArtifact> uml2_deployedartifacts;




    private UML2_DeploymentTarget uml2_deploymenttarget;




    private UML2_DeploymentTarget uml2_deploymenttarget;


    public UML2_Deployment(
    ) {
        super(
        );
        this.uml2_deployedartifacts = new ArrayList<>();
    }

    public UML2_Deployment(
        ArrayList<UML2_DeployedArtifact> uml2_deployedartifacts    ) {
        this.uml2_deployedartifacts = uml2_deployedartifacts;
    }


    public List<UML2_DeployedArtifact> getUml2_deployedartifacts() {
        return uml2_deployedartifacts;
    }

    public void addUml2_deployedartifact(Uml2_deployedartifact uml2_deployedartifact) {
        this.uml2_deployedartifacts.add(uml2_deployedartifact);
    }
    public UML2_DeploymentTarget getUml2_deploymenttarget() {
        return uml2_deploymenttarget;
    }

    public void setUml2_deploymenttarget(UML2_DeploymentTarget uml2_deploymenttarget) {
        this.uml2_deploymenttarget = uml2_deploymenttarget;
    }
    public UML2_DeploymentTarget getUml2_deploymenttarget() {
        return uml2_deploymenttarget;
    }

    public void setUml2_deploymenttarget(UML2_DeploymentTarget uml2_deploymenttarget) {
        this.uml2_deploymenttarget = uml2_deploymenttarget;
    }

}