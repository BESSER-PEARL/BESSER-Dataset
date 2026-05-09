





import java.util.List;
import java.util.ArrayList;

public class GraphML_Graph extends Element {

    private String edgeDefault;



    public GraphML_Graph(
        String edgeDefault    ) {
        super(
        );
        this.edgeDefault = edgeDefault;
    }


    public String getEdgedefault() {
        return edgeDefault;
    }

    public void setEdgedefault(String edgeDefault) {
        this.edgeDefault = edgeDefault;
    }


}