





import java.util.List;
import java.util.ArrayList;

public class graphpattern_EObjectList  {

    private String label;





    private List<graphpattern_EObject> graphpattern_eobjects;


    public graphpattern_EObjectList(
        String label    ) {
        this.label = label;
        this.graphpattern_eobjects = new ArrayList<>();
    }

    public graphpattern_EObjectList(
        String label        ArrayList<graphpattern_EObject> graphpattern_eobjects    ) {
        this.label = label;
        this.graphpattern_eobjects = graphpattern_eobjects;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<graphpattern_EObject> getGraphpattern_eobjects() {
        return graphpattern_eobjects;
    }

    public void addGraphpattern_eobject(Graphpattern_eobject graphpattern_eobject) {
        this.graphpattern_eobjects.add(graphpattern_eobject);
    }

}