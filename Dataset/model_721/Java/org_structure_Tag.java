





import java.util.List;
import java.util.ArrayList;

public class org_structure_Tag extends KermetaModelElement {

    private String name;
    private String value;





    private List<structure_KermetaModelElement> structure_kermetamodelelements;


    public org_structure_Tag(
        String name,        String value    ) {
        super(
        );
        this.name = name;
        this.value = value;
        this.structure_kermetamodelelements = new ArrayList<>();
    }

    public org_structure_Tag(
        String name,        String value        ArrayList<structure_KermetaModelElement> structure_kermetamodelelements    ) {
        this.name = name;
        this.value = value;
        this.structure_kermetamodelelements = structure_kermetamodelelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public List<structure_KermetaModelElement> getStructure_kermetamodelelements() {
        return structure_kermetamodelelements;
    }

    public void addStructure_kermetamodelelement(Structure_kermetamodelelement structure_kermetamodelelement) {
        this.structure_kermetamodelelements.add(structure_kermetamodelelement);
    }

}