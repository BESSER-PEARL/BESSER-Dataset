





import java.util.List;
import java.util.ArrayList;

public class graphpattern_SubGraph extends PatternElement {






    private graphpattern_GraphElement graphpattern_graphelement;




    private graphpattern_SubGraph graphpattern_subgraph;




    private graphpattern_GraphPattern graphpattern_graphpattern;




    private List<graphpattern_GraphElement> graphpattern_graphelements;


    public graphpattern_SubGraph(
    ) {
        super(
        );
        this.graphpattern_graphelements = new ArrayList<>();
    }

    public graphpattern_SubGraph(
        ArrayList<graphpattern_GraphElement> graphpattern_graphelements    ) {
        this.graphpattern_graphelements = graphpattern_graphelements;
    }


    public graphpattern_GraphElement getGraphpattern_graphelement() {
        return graphpattern_graphelement;
    }

    public void setGraphpattern_graphelement(graphpattern_GraphElement graphpattern_graphelement) {
        this.graphpattern_graphelement = graphpattern_graphelement;
    }
    public graphpattern_SubGraph getGraphpattern_subgraph() {
        return graphpattern_subgraph;
    }

    public void setGraphpattern_subgraph(graphpattern_SubGraph graphpattern_subgraph) {
        this.graphpattern_subgraph = graphpattern_subgraph;
    }
    public graphpattern_GraphPattern getGraphpattern_graphpattern() {
        return graphpattern_graphpattern;
    }

    public void setGraphpattern_graphpattern(graphpattern_GraphPattern graphpattern_graphpattern) {
        this.graphpattern_graphpattern = graphpattern_graphpattern;
    }
    public List<graphpattern_GraphElement> getGraphpattern_graphelements() {
        return graphpattern_graphelements;
    }

    public void addGraphpattern_graphelement(Graphpattern_graphelement graphpattern_graphelement) {
        this.graphpattern_graphelements.add(graphpattern_graphelement);
    }

}