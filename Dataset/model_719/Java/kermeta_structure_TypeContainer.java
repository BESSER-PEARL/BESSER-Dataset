





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_TypeContainer extends Object {






    private List<structure_Type> structure_types;


    public kermeta_structure_TypeContainer(
    ) {
        super(
        );
        this.structure_types = new ArrayList<>();
    }

    public kermeta_structure_TypeContainer(
        ArrayList<structure_Type> structure_types    ) {
        this.structure_types = structure_types;
    }


    public List<structure_Type> getStructure_types() {
        return structure_types;
    }

    public void addStructure_type(Structure_type structure_type) {
        this.structure_types.add(structure_type);
    }

}