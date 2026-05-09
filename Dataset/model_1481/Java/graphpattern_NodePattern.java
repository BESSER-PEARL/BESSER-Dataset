





import java.util.List;
import java.util.ArrayList;

public class graphpattern_NodePattern extends GraphElement {






    private graphpattern_GraphPattern graphpattern_graphpattern;




    private List<graphpattern_Association> graphpattern_associations;




    private graphpattern_Association graphpattern_association;


    public graphpattern_NodePattern(
    ) {
        super(
        );
        this.graphpattern_associations = new ArrayList<>();
    }

    public graphpattern_NodePattern(
        ArrayList<graphpattern_Association> graphpattern_associations    ) {
        this.graphpattern_associations = graphpattern_associations;
    }


    public graphpattern_GraphPattern getGraphpattern_graphpattern() {
        return graphpattern_graphpattern;
    }

    public void setGraphpattern_graphpattern(graphpattern_GraphPattern graphpattern_graphpattern) {
        this.graphpattern_graphpattern = graphpattern_graphpattern;
    }
    public List<graphpattern_Association> getGraphpattern_associations() {
        return graphpattern_associations;
    }

    public void addGraphpattern_association(Graphpattern_association graphpattern_association) {
        this.graphpattern_associations.add(graphpattern_association);
    }
    public graphpattern_Association getGraphpattern_association() {
        return graphpattern_association;
    }

    public void setGraphpattern_association(graphpattern_Association graphpattern_association) {
        this.graphpattern_association = graphpattern_association;
    }

}