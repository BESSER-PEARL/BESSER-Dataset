





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_DeploymentTarget extends NamedElement {






    private List<uml3_0_0_PackageableElement> uml3_0_0_packageableelements;


    public uml3_0_0_DeploymentTarget(
    ) {
        super(
        );
        this.uml3_0_0_packageableelements = new ArrayList<>();
    }

    public uml3_0_0_DeploymentTarget(
        ArrayList<uml3_0_0_PackageableElement> uml3_0_0_packageableelements    ) {
        this.uml3_0_0_packageableelements = uml3_0_0_packageableelements;
    }


    public List<uml3_0_0_PackageableElement> getUml3_0_0_packageableelements() {
        return uml3_0_0_packageableelements;
    }

    public void addUml3_0_0_packageableelement(Uml3_0_0_packageableelement uml3_0_0_packageableelement) {
        this.uml3_0_0_packageableelements.add(uml3_0_0_packageableelement);
    }

}