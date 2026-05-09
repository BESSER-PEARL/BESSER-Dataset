





import java.util.List;
import java.util.ArrayList;

public class org_structure_ModelTypeDefinitionBinding extends structure_KermetaModelElement, structure_ModelTypeDefinitionContainer {






    private List<structure_ModelTransformation> structure_modeltransformations;


    public org_structure_ModelTypeDefinitionBinding(
    ) {
        super(
        );
        this.structure_modeltransformations = new ArrayList<>();
    }

    public org_structure_ModelTypeDefinitionBinding(
        ArrayList<structure_ModelTransformation> structure_modeltransformations    ) {
        this.structure_modeltransformations = structure_modeltransformations;
    }


    public List<structure_ModelTransformation> getStructure_modeltransformations() {
        return structure_modeltransformations;
    }

    public void addStructure_modeltransformation(Structure_modeltransformation structure_modeltransformation) {
        this.structure_modeltransformations.add(structure_modeltransformation);
    }

}