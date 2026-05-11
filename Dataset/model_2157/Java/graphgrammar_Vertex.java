





import java.util.List;
import java.util.ArrayList;

public class graphgrammar_Vertex  {

    private String id;





    private graphgrammar_Graph graphgrammar_graph;




    private graphgrammar_VertexToSymbolSymbolsPairMap graphgrammar_vertextosymbolsymbolspairmap;




    private graphgrammar_Symbol graphgrammar_symbol;


    public graphgrammar_Vertex(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public graphgrammar_Graph getGraphgrammar_graph() {
        return graphgrammar_graph;
    }

    public void setGraphgrammar_graph(graphgrammar_Graph graphgrammar_graph) {
        this.graphgrammar_graph = graphgrammar_graph;
    }
    public graphgrammar_VertexToSymbolSymbolsPairMap getGraphgrammar_vertextosymbolsymbolspairmap() {
        return graphgrammar_vertextosymbolsymbolspairmap;
    }

    public void setGraphgrammar_vertextosymbolsymbolspairmap(graphgrammar_VertexToSymbolSymbolsPairMap graphgrammar_vertextosymbolsymbolspairmap) {
        this.graphgrammar_vertextosymbolsymbolspairmap = graphgrammar_vertextosymbolsymbolspairmap;
    }
    public graphgrammar_Symbol getGraphgrammar_symbol() {
        return graphgrammar_symbol;
    }

    public void setGraphgrammar_symbol(graphgrammar_Symbol graphgrammar_symbol) {
        this.graphgrammar_symbol = graphgrammar_symbol;
    }

}