





import java.util.List;
import java.util.ArrayList;

public class trace_Traced_TracedObjects  {






    private List<petrinet_TracedPlace> petrinet_tracedplaces;


    public trace_Traced_TracedObjects(
    ) {
        this.petrinet_tracedplaces = new ArrayList<>();
    }

    public trace_Traced_TracedObjects(
        ArrayList<petrinet_TracedPlace> petrinet_tracedplaces    ) {
        this.petrinet_tracedplaces = petrinet_tracedplaces;
    }


    public List<petrinet_TracedPlace> getPetrinet_tracedplaces() {
        return petrinet_tracedplaces;
    }

    public void addPetrinet_tracedplace(Petrinet_tracedplace petrinet_tracedplace) {
        this.petrinet_tracedplaces.add(petrinet_tracedplace);
    }

}