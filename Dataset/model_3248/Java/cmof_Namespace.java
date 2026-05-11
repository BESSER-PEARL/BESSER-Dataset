





import java.util.List;
import java.util.ArrayList;

public class cmof_Namespace extends NamedElement {






    private List<cmof_PackageableElement> cmof_packageableelements;


    public cmof_Namespace(
    ) {
        super(
        );
        this.cmof_packageableelements = new ArrayList<>();
    }

    public cmof_Namespace(
        ArrayList<cmof_PackageableElement> cmof_packageableelements    ) {
        this.cmof_packageableelements = cmof_packageableelements;
    }


    public List<cmof_PackageableElement> getCmof_packageableelements() {
        return cmof_packageableelements;
    }

    public void addCmof_packageableelement(Cmof_packageableelement cmof_packageableelement) {
        this.cmof_packageableelements.add(cmof_packageableelement);
    }

}