





import java.util.List;
import java.util.ArrayList;

public class graph_DocumentRoot  {

    private String mixed;





    private List<graph_DependencyGraph> graph_dependencygraphs;


    public graph_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.graph_dependencygraphs = new ArrayList<>();
    }

    public graph_DocumentRoot(
        String mixed        ArrayList<graph_DependencyGraph> graph_dependencygraphs    ) {
        this.mixed = mixed;
        this.graph_dependencygraphs = graph_dependencygraphs;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<graph_DependencyGraph> getGraph_dependencygraphs() {
        return graph_dependencygraphs;
    }

    public void addGraph_dependencygraph(Graph_dependencygraph graph_dependencygraph) {
        this.graph_dependencygraphs.add(graph_dependencygraph);
    }

}