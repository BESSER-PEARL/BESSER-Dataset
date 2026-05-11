





import java.util.List;
import java.util.ArrayList;

public class graphgrammar_ZoneVertex extends Vertex {






    private graphgrammar_ParsingTree graphgrammar_parsingtree;




    private List<graphgrammar_Vertex> graphgrammar_vertexs;




    private List<graphgrammar_Vertex> graphgrammar_vertexs;


    public graphgrammar_ZoneVertex(
    ) {
        super(
        );
        this.graphgrammar_vertexs = new ArrayList<>();
        this.graphgrammar_vertexs = new ArrayList<>();
    }

    public graphgrammar_ZoneVertex(
        ArrayList<graphgrammar_Vertex> graphgrammar_vertexs,        ArrayList<graphgrammar_Vertex> graphgrammar_vertexs    ) {
        this.graphgrammar_vertexs = graphgrammar_vertexs;
        this.graphgrammar_vertexs = graphgrammar_vertexs;
    }


    public graphgrammar_ParsingTree getGraphgrammar_parsingtree() {
        return graphgrammar_parsingtree;
    }

    public void setGraphgrammar_parsingtree(graphgrammar_ParsingTree graphgrammar_parsingtree) {
        this.graphgrammar_parsingtree = graphgrammar_parsingtree;
    }
    public List<graphgrammar_Vertex> getGraphgrammar_vertexs() {
        return graphgrammar_vertexs;
    }

    public void addGraphgrammar_vertex(Graphgrammar_vertex graphgrammar_vertex) {
        this.graphgrammar_vertexs.add(graphgrammar_vertex);
    }
    public List<graphgrammar_Vertex> getGraphgrammar_vertexs() {
        return graphgrammar_vertexs;
    }

    public void addGraphgrammar_vertex(Graphgrammar_vertex graphgrammar_vertex) {
        this.graphgrammar_vertexs.add(graphgrammar_vertex);
    }

}