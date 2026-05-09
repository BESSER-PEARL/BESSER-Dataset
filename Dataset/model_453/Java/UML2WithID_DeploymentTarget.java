





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_DeploymentTarget extends NamedElement {






    private List<UML2WithID_PackageableElement> uml2withid_packageableelements;


    public UML2WithID_DeploymentTarget(
    ) {
        super(
        );
        this.uml2withid_packageableelements = new ArrayList<>();
    }

    public UML2WithID_DeploymentTarget(
        ArrayList<UML2WithID_PackageableElement> uml2withid_packageableelements    ) {
        this.uml2withid_packageableelements = uml2withid_packageableelements;
    }


    public List<UML2WithID_PackageableElement> getUml2withid_packageableelements() {
        return uml2withid_packageableelements;
    }

    public void addUml2withid_packageableelement(Uml2withid_packageableelement uml2withid_packageableelement) {
        this.uml2withid_packageableelements.add(uml2withid_packageableelement);
    }

}