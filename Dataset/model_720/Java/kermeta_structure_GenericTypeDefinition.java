





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_GenericTypeDefinition extends TypeDefinition {






    private List<structure_TypeVariable> structure_typevariables;


    public kermeta_structure_GenericTypeDefinition(
    ) {
        super(
        );
        this.structure_typevariables = new ArrayList<>();
    }

    public kermeta_structure_GenericTypeDefinition(
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