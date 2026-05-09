





import java.util.List;
import java.util.ArrayList;

public class org_structure_Model extends KermetaModelElement {






    private List<structure_KermetaModelElement> structure_kermetamodelelements;


    public org_structure_Model(
    ) {
        super(
        );
        this.structure_kermetamodelelements = new ArrayList<>();
    }

    public org_structure_Model(
        ArrayList<structure_KermetaModelElement> structure_kermetamodelelements    ) {
        this.structure_kermetamodelelements = structure_kermetamodelelements;
    }


    public List<structure_KermetaModelElement> getStructure_kermetamodelelements() {
        return structure_kermetamodelelements;
    }

    public void addStructure_kermetamodelelement(Structure_kermetamodelelement structure_kermetamodelelement) {
        this.structure_kermetamodelelements.add(structure_kermetamodelelement);
    }

}