





import java.util.List;
import java.util.ArrayList;

public class org_structure_UseAdaptationOperator extends KermetaModelElement {






    private List<structure_KermetaModelElement> structure_kermetamodelelements;




    private structure_AdaptationOperator structure_adaptationoperator;


    public org_structure_UseAdaptationOperator(
    ) {
        super(
        );
        this.structure_kermetamodelelements = new ArrayList<>();
    }

    public org_structure_UseAdaptationOperator(
        ArrayList<structure_KermetaModelElement> structure_kermetamodelelements    ) {
        this.structure_kermetamodelelements = structure_kermetamodelelements;
    }


    public List<structure_KermetaModelElement> getStructure_kermetamodelelements() {
        return structure_kermetamodelelements;
    }

    public void addStructure_kermetamodelelement(Structure_kermetamodelelement structure_kermetamodelelement) {
        this.structure_kermetamodelelements.add(structure_kermetamodelelement);
    }
    public structure_AdaptationOperator getStructure_adaptationoperator() {
        return structure_adaptationoperator;
    }

    public void setStructure_adaptationoperator(structure_AdaptationOperator structure_adaptationoperator) {
        this.structure_adaptationoperator = structure_adaptationoperator;
    }

}