





import java.util.List;
import java.util.ArrayList;

public class graphpattern_Resource  {






    private List<graphpattern_EObject> graphpattern_eobjects;


    public graphpattern_Resource(
    ) {
        this.graphpattern_eobjects = new ArrayList<>();
    }

    public graphpattern_Resource(
        ArrayList<graphpattern_EObject> graphpattern_eobjects    ) {
        this.graphpattern_eobjects = graphpattern_eobjects;
    }


    public List<graphpattern_EObject> getGraphpattern_eobjects() {
        return graphpattern_eobjects;
    }

    public void addGraphpattern_eobject(Graphpattern_eobject graphpattern_eobject) {
        this.graphpattern_eobjects.add(graphpattern_eobject);
    }

}