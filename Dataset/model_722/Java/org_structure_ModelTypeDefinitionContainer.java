





import java.util.List;
import java.util.ArrayList;

public class org_structure_ModelTypeDefinitionContainer extends KermetaModelElement {






    private List<structure_ModelTypeDefinition> structure_modeltypedefinitions;


    public org_structure_ModelTypeDefinitionContainer(
    ) {
        super(
        );
        this.structure_modeltypedefinitions = new ArrayList<>();
    }

    public org_structure_ModelTypeDefinitionContainer(
        ArrayList<structure_ModelTypeDefinition> structure_modeltypedefinitions    ) {
        this.structure_modeltypedefinitions = structure_modeltypedefinitions;
    }


    public List<structure_ModelTypeDefinition> getStructure_modeltypedefinitions() {
        return structure_modeltypedefinitions;
    }

    public void addStructure_modeltypedefinition(Structure_modeltypedefinition structure_modeltypedefinition) {
        this.structure_modeltypedefinitions.add(structure_modeltypedefinition);
    }

}