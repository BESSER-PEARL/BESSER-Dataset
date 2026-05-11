





import java.util.List;
import java.util.ArrayList;

public class OO_concept_Package extends NamedElement, PackageableElement {






    private List<OO_concept_PackageableElement> oo_concept_packageableelements;


    public OO_concept_Package(
    ) {
        super(
        );
        this.oo_concept_packageableelements = new ArrayList<>();
    }

    public OO_concept_Package(
        ArrayList<OO_concept_PackageableElement> oo_concept_packageableelements    ) {
        this.oo_concept_packageableelements = oo_concept_packageableelements;
    }


    public List<OO_concept_PackageableElement> getOo_concept_packageableelements() {
        return oo_concept_packageableelements;
    }

    public void addOo_concept_packageableelement(Oo_concept_packageableelement oo_concept_packageableelement) {
        this.oo_concept_packageableelements.add(oo_concept_packageableelement);
    }

}