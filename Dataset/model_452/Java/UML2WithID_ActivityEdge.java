





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ActivityEdge extends RedefinableElement {






    private List<UML2WithID_ActivityEdge> uml2withid_activityedges;


    public UML2WithID_ActivityEdge(
    ) {
        super(
        );
        this.uml2withid_activityedges = new ArrayList<>();
    }

    public UML2WithID_ActivityEdge(
        ArrayList<UML2WithID_ActivityEdge> uml2withid_activityedges    ) {
        this.uml2withid_activityedges = uml2withid_activityedges;
    }


    public List<UML2WithID_ActivityEdge> getUml2withid_activityedges() {
        return uml2withid_activityedges;
    }

    public void addUml2withid_activityedge(Uml2withid_activityedge uml2withid_activityedge) {
        this.uml2withid_activityedges.add(uml2withid_activityedge);
    }

}