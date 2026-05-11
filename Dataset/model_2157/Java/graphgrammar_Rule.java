





import java.util.List;
import java.util.ArrayList;

public class graphgrammar_Rule  {

    private String id;
    private String name;





    private graphgrammar_Grammar graphgrammar_grammar;




    private graphgrammar_Symbol graphgrammar_symbol;




    private graphgrammar_Graph graphgrammar_graph;




    private List<graphgrammar_VertexToSymbolSymbolsPairMap> graphgrammar_vertextosymbolsymbolspairmaps;




    private List<graphgrammar_Vertex> graphgrammar_vertexs;


    public graphgrammar_Rule(
        String id,        String name    ) {
        this.id = id;
        this.name = name;
        this.graphgrammar_vertextosymbolsymbolspairmaps = new ArrayList<>();
        this.graphgrammar_vertexs = new ArrayList<>();
    }

    public graphgrammar_Rule(
        String id,        String name        ArrayList<graphgrammar_VertexToSymbolSymbolsPairMap> graphgrammar_vertextosymbolsymbolspairmaps,        ArrayList<graphgrammar_Vertex> graphgrammar_vertexs    ) {
        this.id = id;
        this.name = name;
        this.graphgrammar_vertextosymbolsymbolspairmaps = graphgrammar_vertextosymbolsymbolspairmaps;
        this.graphgrammar_vertexs = graphgrammar_vertexs;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public graphgrammar_Grammar getGraphgrammar_grammar() {
        return graphgrammar_grammar;
    }

    public void setGraphgrammar_grammar(graphgrammar_Grammar graphgrammar_grammar) {
        this.graphgrammar_grammar = graphgrammar_grammar;
    }
    public graphgrammar_Symbol getGraphgrammar_symbol() {
        return graphgrammar_symbol;
    }

    public void setGraphgrammar_symbol(graphgrammar_Symbol graphgrammar_symbol) {
        this.graphgrammar_symbol = graphgrammar_symbol;
    }
    public graphgrammar_Graph getGraphgrammar_graph() {
        return graphgrammar_graph;
    }

    public void setGraphgrammar_graph(graphgrammar_Graph graphgrammar_graph) {
        this.graphgrammar_graph = graphgrammar_graph;
    }
    public List<graphgrammar_VertexToSymbolSymbolsPairMap> getGraphgrammar_vertextosymbolsymbolspairmaps() {
        return graphgrammar_vertextosymbolsymbolspairmaps;
    }

    public void addGraphgrammar_vertextosymbolsymbolspairmap(Graphgrammar_vertextosymbolsymbolspairmap graphgrammar_vertextosymbolsymbolspairmap) {
        this.graphgrammar_vertextosymbolsymbolspairmaps.add(graphgrammar_vertextosymbolsymbolspairmap);
    }
    public List<graphgrammar_Vertex> getGraphgrammar_vertexs() {
        return graphgrammar_vertexs;
    }

    public void addGraphgrammar_vertex(Graphgrammar_vertex graphgrammar_vertex) {
        this.graphgrammar_vertexs.add(graphgrammar_vertex);
    }

}