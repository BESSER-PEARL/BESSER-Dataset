





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_Model extends Object {






    private List<structure_Object> structure_objects;


    public kermeta_structure_Model(
    ) {
        super(
        );
        this.structure_objects = new ArrayList<>();
    }

    public kermeta_structure_Model(
        ArrayList<structure_Object> structure_objects    ) {
        this.structure_objects = structure_objects;
    }


    public List<structure_Object> getStructure_objects() {
        return structure_objects;
    }

    public void addStructure_object(Structure_object structure_object) {
        this.structure_objects.add(structure_object);
    }

}