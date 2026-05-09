





import java.util.List;
import java.util.ArrayList;

public class org_structure_VirtualType extends ObjectTypeVariable {






    private structure_ModelElementTypeDefinition structure_modelelementtypedefinition;




    private List<structure_TypeVariableBinding> structure_typevariablebindings;


    public org_structure_VirtualType(
    ) {
        super(
        );
        this.structure_typevariablebindings = new ArrayList<>();
    }

    public org_structure_VirtualType(
        ArrayList<structure_TypeVariableBinding> structure_typevariablebindings    ) {
        this.structure_typevariablebindings = structure_typevariablebindings;
    }


    public structure_ModelElementTypeDefinition getStructure_modelelementtypedefinition() {
        return structure_modelelementtypedefinition;
    }

    public void setStructure_modelelementtypedefinition(structure_ModelElementTypeDefinition structure_modelelementtypedefinition) {
        this.structure_modelelementtypedefinition = structure_modelelementtypedefinition;
    }
    public List<structure_TypeVariableBinding> getStructure_typevariablebindings() {
        return structure_typevariablebindings;
    }

    public void addStructure_typevariablebinding(Structure_typevariablebinding structure_typevariablebinding) {
        this.structure_typevariablebindings.add(structure_typevariablebinding);
    }

}