





import java.util.List;
import java.util.ArrayList;

public class gmf_all_mappings_CompartmentMapping  {






    private NodeMapping nodemapping;




    private List<ChildReference> childreferences;


    public gmf_all_mappings_CompartmentMapping(
    ) {
        this.childreferences = new ArrayList<>();
    }

    public gmf_all_mappings_CompartmentMapping(
        ArrayList<ChildReference> childreferences    ) {
        this.childreferences = childreferences;
    }


    public NodeMapping getNodemapping() {
        return nodemapping;
    }

    public void setNodemapping(NodeMapping nodemapping) {
        this.nodemapping = nodemapping;
    }
    public List<ChildReference> getChildreferences() {
        return childreferences;
    }

    public void addChildreference(Childreference childreference) {
        this.childreferences.add(childreference);
    }

}