





import java.util.List;
import java.util.ArrayList;

public class graphpattern_DependencyNode  {






    private List<graphpattern_NodePattern> graphpattern_nodepatterns;




    private graphpattern_DependencyGraph graphpattern_dependencygraph;




    private graphpattern_DependencyGraph graphpattern_dependencygraph;


    public graphpattern_DependencyNode(
    ) {
        this.graphpattern_nodepatterns = new ArrayList<>();
    }

    public graphpattern_DependencyNode(
        ArrayList<graphpattern_NodePattern> graphpattern_nodepatterns    ) {
        this.graphpattern_nodepatterns = graphpattern_nodepatterns;
    }


    public List<graphpattern_NodePattern> getGraphpattern_nodepatterns() {
        return graphpattern_nodepatterns;
    }

    public void addGraphpattern_nodepattern(Graphpattern_nodepattern graphpattern_nodepattern) {
        this.graphpattern_nodepatterns.add(graphpattern_nodepattern);
    }
    public graphpattern_DependencyGraph getGraphpattern_dependencygraph() {
        return graphpattern_dependencygraph;
    }

    public void setGraphpattern_dependencygraph(graphpattern_DependencyGraph graphpattern_dependencygraph) {
        this.graphpattern_dependencygraph = graphpattern_dependencygraph;
    }
    public graphpattern_DependencyGraph getGraphpattern_dependencygraph() {
        return graphpattern_dependencygraph;
    }

    public void setGraphpattern_dependencygraph(graphpattern_DependencyGraph graphpattern_dependencygraph) {
        this.graphpattern_dependencygraph = graphpattern_dependencygraph;
    }

}