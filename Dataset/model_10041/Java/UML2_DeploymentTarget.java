





import java.util.List;
import java.util.ArrayList;

public class UML2_DeploymentTarget extends NamedElement {






    private List<UML2_PackageableElement> uml2_packageableelements;


    public UML2_DeploymentTarget(
    ) {
        super(
        );
        this.uml2_packageableelements = new ArrayList<>();
    }

    public UML2_DeploymentTarget(
        ArrayList<UML2_PackageableElement> uml2_packageableelements    ) {
        this.uml2_packageableelements = uml2_packageableelements;
    }


    public List<UML2_PackageableElement> getUml2_packageableelements() {
        return uml2_packageableelements;
    }

    public void addUml2_packageableelement(Uml2_packageableelement uml2_packageableelement) {
        this.uml2_packageableelements.add(uml2_packageableelement);
    }

}