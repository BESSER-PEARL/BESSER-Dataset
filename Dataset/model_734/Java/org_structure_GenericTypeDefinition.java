





import java.util.List;
import java.util.ArrayList;

public class org_structure_GenericTypeDefinition extends ModelElementTypeDefinition {






    private List<structure_TypeVariable> structure_typevariables;


    public org_structure_GenericTypeDefinition(
    ) {
        super(
        );
        this.structure_typevariables = new ArrayList<>();
    }

    public org_structure_GenericTypeDefinition(
        ArrayList<structure_TypeVariable> structure_typevariables    ) {
        this.structure_typevariables = structure_typevariables;
    }


    public List<structure_TypeVariable> getStructure_typevariables() {
        return structure_typevariables;
    }

    public void addStructure_typevariable(Structure_typevariable structure_typevariable) {
        this.structure_typevariables.add(structure_typevariable);
    }

}