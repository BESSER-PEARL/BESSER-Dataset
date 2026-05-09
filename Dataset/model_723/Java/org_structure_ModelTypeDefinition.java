





import java.util.List;
import java.util.ArrayList;

public class org_structure_ModelTypeDefinition extends TypeDefinition {






    private List<structure_ModelElementTypeDefinition> structure_modelelementtypedefinitions;




    private List<structure_ModelTransformation> structure_modeltransformations;


    public org_structure_ModelTypeDefinition(
    ) {
        super(
        );
        this.structure_modelelementtypedefinitions = new ArrayList<>();
        this.structure_modeltransformations = new ArrayList<>();
    }

    public org_structure_ModelTypeDefinition(
        ArrayList<structure_ModelElementTypeDefinition> structure_modelelementtypedefinitions,        ArrayList<structure_ModelTransformation> structure_modeltransformations    ) {
        this.structure_modelelementtypedefinitions = structure_modelelementtypedefinitions;
        this.structure_modeltransformations = structure_modeltransformations;
    }


    public List<structure_ModelElementTypeDefinition> getStructure_modelelementtypedefinitions() {
        return structure_modelelementtypedefinitions;
    }

    public void addStructure_modelelementtypedefinition(Structure_modelelementtypedefinition structure_modelelementtypedefinition) {
        this.structure_modelelementtypedefinitions.add(structure_modelelementtypedefinition);
    }
    public List<structure_ModelTransformation> getStructure_modeltransformations() {
        return structure_modeltransformations;
    }

    public void addStructure_modeltransformation(Structure_modeltransformation structure_modeltransformation) {
        this.structure_modeltransformations.add(structure_modeltransformation);
    }

}