





import java.util.List;
import java.util.ArrayList;

public class org_structure_UseAdaptationOperator extends KermetaModelElement {






    private List<structure_KermetaModelElement> structure_kermetamodelelements;




    private List<structure_UnresolvedReference> structure_unresolvedreferences;


    public org_structure_UseAdaptationOperator(
    ) {
        super(
        );
        this.structure_kermetamodelelements = new ArrayList<>();
        this.structure_unresolvedreferences = new ArrayList<>();
    }

    public org_structure_UseAdaptationOperator(
        ArrayList<structure_KermetaModelElement> structure_kermetamodelelements,        ArrayList<structure_UnresolvedReference> structure_unresolvedreferences    ) {
        this.structure_kermetamodelelements = structure_kermetamodelelements;
        this.structure_unresolvedreferences = structure_unresolvedreferences;
    }


    public List<structure_KermetaModelElement> getStructure_kermetamodelelements() {
        return structure_kermetamodelelements;
    }

    public void addStructure_kermetamodelelement(Structure_kermetamodelelement structure_kermetamodelelement) {
        this.structure_kermetamodelelements.add(structure_kermetamodelelement);
    }
    public List<structure_UnresolvedReference> getStructure_unresolvedreferences() {
        return structure_unresolvedreferences;
    }

    public void addStructure_unresolvedreference(Structure_unresolvedreference structure_unresolvedreference) {
        this.structure_unresolvedreferences.add(structure_unresolvedreference);
    }

}