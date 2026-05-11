





import java.util.List;
import java.util.ArrayList;

public class sequence_ordering_InstanceRolesOrdering  {






    private List<ordering_sequence_EObject> ordering_sequence_eobjects;


    public sequence_ordering_InstanceRolesOrdering(
    ) {
        this.ordering_sequence_eobjects = new ArrayList<>();
    }

    public sequence_ordering_InstanceRolesOrdering(
        ArrayList<ordering_sequence_EObject> ordering_sequence_eobjects    ) {
        this.ordering_sequence_eobjects = ordering_sequence_eobjects;
    }


    public List<ordering_sequence_EObject> getOrdering_sequence_eobjects() {
        return ordering_sequence_eobjects;
    }

    public void addOrdering_sequence_eobject(Ordering_sequence_eobject ordering_sequence_eobject) {
        this.ordering_sequence_eobjects.add(ordering_sequence_eobject);
    }

}