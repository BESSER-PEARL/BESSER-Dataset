





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_Tag extends Object {

    private String value;
    private String name;





    private List<structure_Object> structure_objects;


    public kermeta_structure_Tag(
        String value,        String name    ) {
        super(
        );
        this.value = value;
        this.name = name;
        this.structure_objects = new ArrayList<>();
    }

    public kermeta_structure_Tag(
        String value,        String name        ArrayList<structure_Object> structure_objects    ) {
        this.value = value;
        this.name = name;
        this.structure_objects = structure_objects;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<structure_Object> getStructure_objects() {
        return structure_objects;
    }

    public void addStructure_object(Structure_object structure_object) {
        this.structure_objects.add(structure_object);
    }

}