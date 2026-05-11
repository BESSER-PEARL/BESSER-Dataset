





import java.util.List;
import java.util.ArrayList;

public class graphgrammar_StringToVertexMap  {

    private String key;





    private graphgrammar_Vertex graphgrammar_vertex;




    private graphgrammar_Resolution graphgrammar_resolution;


    public graphgrammar_StringToVertexMap(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public graphgrammar_Vertex getGraphgrammar_vertex() {
        return graphgrammar_vertex;
    }

    public void setGraphgrammar_vertex(graphgrammar_Vertex graphgrammar_vertex) {
        this.graphgrammar_vertex = graphgrammar_vertex;
    }
    public graphgrammar_Resolution getGraphgrammar_resolution() {
        return graphgrammar_resolution;
    }

    public void setGraphgrammar_resolution(graphgrammar_Resolution graphgrammar_resolution) {
        this.graphgrammar_resolution = graphgrammar_resolution;
    }

}