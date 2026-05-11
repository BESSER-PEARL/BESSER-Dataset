





import java.util.List;
import java.util.ArrayList;

public class gmf_all_mappings_NodeMapping extends mappings_ToolOwner, mappings_MappingEntry, mappings_AppearanceSteward, mappings_MenuOwner {






    private List<ChildReference> childreferences;




    private List<CompartmentMapping> compartmentmappings;


    public gmf_all_mappings_NodeMapping(
    ) {
        super(
        );
        this.childreferences = new ArrayList<>();
        this.compartmentmappings = new ArrayList<>();
    }

    public gmf_all_mappings_NodeMapping(
        ArrayList<ChildReference> childreferences,        ArrayList<CompartmentMapping> compartmentmappings    ) {
        this.childreferences = childreferences;
        this.compartmentmappings = compartmentmappings;
    }


    public List<ChildReference> getChildreferences() {
        return childreferences;
    }

    public void addChildreference(Childreference childreference) {
        this.childreferences.add(childreference);
    }
    public List<CompartmentMapping> getCompartmentmappings() {
        return compartmentmappings;
    }

    public void addCompartmentmapping(Compartmentmapping compartmentmapping) {
        this.compartmentmappings.add(compartmentmapping);
    }

}