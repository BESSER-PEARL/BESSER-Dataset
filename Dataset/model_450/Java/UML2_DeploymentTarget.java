





import java.util.List;
import java.util.ArrayList;

public class UML2_DeploymentTarget extends NamedElement {






    private UML2_Deployment uml2_deployment;




    private List<UML2_PackageableElement> uml2_packageableelements;




    private List<UML2_Deployment> uml2_deployments;


    public UML2_DeploymentTarget(
    ) {
        super(
        );
        this.uml2_packageableelements = new ArrayList<>();
        this.uml2_deployments = new ArrayList<>();
    }

    public UML2_DeploymentTarget(
        ArrayList<UML2_PackageableElement> uml2_packageableelements,        ArrayList<UML2_Deployment> uml2_deployments    ) {
        this.uml2_packageableelements = uml2_packageableelements;
        this.uml2_deployments = uml2_deployments;
    }


    public UML2_Deployment getUml2_deployment() {
        return uml2_deployment;
    }

    public void setUml2_deployment(UML2_Deployment uml2_deployment) {
        this.uml2_deployment = uml2_deployment;
    }
    public List<UML2_PackageableElement> getUml2_packageableelements() {
        return uml2_packageableelements;
    }

    public void addUml2_packageableelement(Uml2_packageableelement uml2_packageableelement) {
        this.uml2_packageableelements.add(uml2_packageableelement);
    }
    public List<UML2_Deployment> getUml2_deployments() {
        return uml2_deployments;
    }

    public void addUml2_deployment(Uml2_deployment uml2_deployment) {
        this.uml2_deployments.add(uml2_deployment);
    }

}