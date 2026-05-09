





import java.util.List;
import java.util.ArrayList;

public class org_structure_ModelTypeDefinition extends TypeDefinition {






    private List<structure_ModelTransformation> structure_modeltransformations;




    private List<structure_ModelElementTypeDefinition> structure_modelelementtypedefinitions;




    private structure_Metamodel structure_metamodel;


    public org_structure_ModelTypeDefinition(
    ) {
        super(
        );
        this.structure_modeltransformations = new ArrayList<>();
        this.structure_modelelementtypedefinitions = new ArrayList<>();
    }

    public org_structure_ModelTypeDefinition(
        ArrayList<structure_ModelTransformation> structure_modeltransformations,        ArrayList<structure_ModelElementTypeDefinition> structure_modelelementtypedefinitions    ) {
        this.structure_modeltransformations = structure_modeltransformations;
        this.structure_modelelementtypedefinitions = structure_modelelementtypedefinitions;
    }


    public List<structure_ModelTransformation> getStructure_modeltransformations() {
        return structure_modeltransformations;
    }

    public void addStructure_modeltransformation(Structure_modeltransformation structure_modeltransformation) {
        this.structure_modeltransformations.add(structure_modeltransformation);
    }
    public List<structure_ModelElementTypeDefinition> getStructure_modelelementtypedefinitions() {
        return structure_modelelementtypedefinitions;
    }

    public void addStructure_modelelementtypedefinition(Structure_modelelementtypedefinition structure_modelelementtypedefinition) {
        this.structure_modelelementtypedefinitions.add(structure_modelelementtypedefinition);
    }
    public structure_Metamodel getStructure_metamodel() {
        return structure_metamodel;
    }

    public void setStructure_metamodel(structure_Metamodel structure_metamodel) {
        this.structure_metamodel = structure_metamodel;
    }

}