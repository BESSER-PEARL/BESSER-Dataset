





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_VirtualType extends ObjectTypeVariable {






    private List<structure_TypeVariableBinding> structure_typevariablebindings;




    private structure_ClassDefinition structure_classdefinition;


    public kermeta_structure_VirtualType(
    ) {
        super(
        );
        this.structure_typevariablebindings = new ArrayList<>();
    }

    public kermeta_structure_VirtualType(
        ArrayList<structure_TypeVariableBinding> structure_typevariablebindings    ) {
        this.structure_typevariablebindings = structure_typevariablebindings;
    }


    public List<structure_TypeVariableBinding> getStructure_typevariablebindings() {
        return structure_typevariablebindings;
    }

    public void addStructure_typevariablebinding(Structure_typevariablebinding structure_typevariablebinding) {
        this.structure_typevariablebindings.add(structure_typevariablebinding);
    }
    public structure_ClassDefinition getStructure_classdefinition() {
        return structure_classdefinition;
    }

    public void setStructure_classdefinition(structure_ClassDefinition structure_classdefinition) {
        this.structure_classdefinition = structure_classdefinition;
    }

}