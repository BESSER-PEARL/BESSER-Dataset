





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_DeploymentTarget extends NamedElement {






    private UML2WithID_Deployment uml2withid_deployment;




    private List<UML2WithID_Deployment> uml2withid_deployments;


    public UML2WithID_DeploymentTarget(
    ) {
        super(
        );
        this.uml2withid_deployments = new ArrayList<>();
    }

    public UML2WithID_DeploymentTarget(
        ArrayList<UML2WithID_Deployment> uml2withid_deployments    ) {
        this.uml2withid_deployments = uml2withid_deployments;
    }


    public UML2WithID_Deployment getUml2withid_deployment() {
        return uml2withid_deployment;
    }

    public void setUml2withid_deployment(UML2WithID_Deployment uml2withid_deployment) {
        this.uml2withid_deployment = uml2withid_deployment;
    }
    public List<UML2WithID_Deployment> getUml2withid_deployments() {
        return uml2withid_deployments;
    }

    public void addUml2withid_deployment(Uml2withid_deployment uml2withid_deployment) {
        this.uml2withid_deployments.add(uml2withid_deployment);
    }

}