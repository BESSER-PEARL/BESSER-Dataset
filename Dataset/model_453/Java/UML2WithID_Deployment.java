





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Deployment extends Dependency {






    private List<UML2WithID_DeployedArtifact> uml2withid_deployedartifacts;




    private UML2WithID_DeploymentTarget uml2withid_deploymenttarget;




    private UML2WithID_DeploymentTarget uml2withid_deploymenttarget;


    public UML2WithID_Deployment(
    ) {
        super(
        );
        this.uml2withid_deployedartifacts = new ArrayList<>();
    }

    public UML2WithID_Deployment(
        ArrayList<UML2WithID_DeployedArtifact> uml2withid_deployedartifacts    ) {
        this.uml2withid_deployedartifacts = uml2withid_deployedartifacts;
    }


    public List<UML2WithID_DeployedArtifact> getUml2withid_deployedartifacts() {
        return uml2withid_deployedartifacts;
    }

    public void addUml2withid_deployedartifact(Uml2withid_deployedartifact uml2withid_deployedartifact) {
        this.uml2withid_deployedartifacts.add(uml2withid_deployedartifact);
    }
    public UML2WithID_DeploymentTarget getUml2withid_deploymenttarget() {
        return uml2withid_deploymenttarget;
    }

    public void setUml2withid_deploymenttarget(UML2WithID_DeploymentTarget uml2withid_deploymenttarget) {
        this.uml2withid_deploymenttarget = uml2withid_deploymenttarget;
    }
    public UML2WithID_DeploymentTarget getUml2withid_deploymenttarget() {
        return uml2withid_deploymenttarget;
    }

    public void setUml2withid_deploymenttarget(UML2WithID_DeploymentTarget uml2withid_deploymenttarget) {
        this.uml2withid_deploymenttarget = uml2withid_deploymenttarget;
    }

}