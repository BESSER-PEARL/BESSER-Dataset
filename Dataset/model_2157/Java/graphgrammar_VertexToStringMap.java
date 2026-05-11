





import java.util.List;
import java.util.ArrayList;

public class graphgrammar_VertexToStringMap  {

    private String value;





    private graphgrammar_ResolutionStep graphgrammar_resolutionstep;




    private graphgrammar_Vertex graphgrammar_vertex;


    public graphgrammar_VertexToStringMap(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public graphgrammar_ResolutionStep getGraphgrammar_resolutionstep() {
        return graphgrammar_resolutionstep;
    }

    public void setGraphgrammar_resolutionstep(graphgrammar_ResolutionStep graphgrammar_resolutionstep) {
        this.graphgrammar_resolutionstep = graphgrammar_resolutionstep;
    }
    public graphgrammar_Vertex getGraphgrammar_vertex() {
        return graphgrammar_vertex;
    }

    public void setGraphgrammar_vertex(graphgrammar_Vertex graphgrammar_vertex) {
        this.graphgrammar_vertex = graphgrammar_vertex;
    }

}