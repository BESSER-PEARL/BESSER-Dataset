





import java.util.List;
import java.util.ArrayList;

public class sgraph_Region extends NamedElement {

    private int priority;





    private sgraph_Vertex sgraph_vertex;




    private List<sgraph_Vertex> sgraph_vertexs;


    public sgraph_Region(
        int priority    ) {
        super(
        );
        this.priority = priority;
        this.sgraph_vertexs = new ArrayList<>();
    }

    public sgraph_Region(
        int priority        ArrayList<sgraph_Vertex> sgraph_vertexs    ) {
        this.priority = priority;
        this.sgraph_vertexs = sgraph_vertexs;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public sgraph_Vertex getSgraph_vertex() {
        return sgraph_vertex;
    }

    public void setSgraph_vertex(sgraph_Vertex sgraph_vertex) {
        this.sgraph_vertex = sgraph_vertex;
    }
    public List<sgraph_Vertex> getSgraph_vertexs() {
        return sgraph_vertexs;
    }

    public void addSgraph_vertex(Sgraph_vertex sgraph_vertex) {
        this.sgraph_vertexs.add(sgraph_vertex);
    }

}