





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_TypeDefinitionContainer extends NamedElement {






    private List<structure_TypeDefinition> structure_typedefinitions;


    public kermeta_structure_TypeDefinitionContainer(
    ) {
        super(
        );
        this.structure_typedefinitions = new ArrayList<>();
    }

    public kermeta_structure_TypeDefinitionContainer(
        ArrayList<structure_TypeDefinition> structure_typedefinitions    ) {
        this.structure_typedefinitions = structure_typedefinitions;
    }


    public List<structure_TypeDefinition> getStructure_typedefinitions() {
        return structure_typedefinitions;
    }

    public void addStructure_typedefinition(Structure_typedefinition structure_typedefinition) {
        this.structure_typedefinitions.add(structure_typedefinition);
    }

}