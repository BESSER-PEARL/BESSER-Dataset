





import java.util.List;
import java.util.ArrayList;

public class cmof_Namespace extends NamedElement {






    private List<cmof_NamedElement> cmof_namedelements;




    private List<cmof_PackageableElement> cmof_packageableelements;


    public cmof_Namespace(
    ) {
        super(
        );
        this.cmof_namedelements = new ArrayList<>();
        this.cmof_packageableelements = new ArrayList<>();
    }

    public cmof_Namespace(
        ArrayList<cmof_NamedElement> cmof_namedelements,        ArrayList<cmof_PackageableElement> cmof_packageableelements    ) {
        this.cmof_namedelements = cmof_namedelements;
        this.cmof_packageableelements = cmof_packageableelements;
    }


    public List<cmof_NamedElement> getCmof_namedelements() {
        return cmof_namedelements;
    }

    public void addCmof_namedelement(Cmof_namedelement cmof_namedelement) {
        this.cmof_namedelements.add(cmof_namedelement);
    }
    public List<cmof_PackageableElement> getCmof_packageableelements() {
        return cmof_packageableelements;
    }

    public void addCmof_packageableelement(Cmof_packageableelement cmof_packageableelement) {
        this.cmof_packageableelements.add(cmof_packageableelement);
    }

}