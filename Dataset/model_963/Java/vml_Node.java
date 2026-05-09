





import java.util.List;
import java.util.ArrayList;

public class vml_Node extends DiagramElement {

    private String title;
    private String icone;





    private List<vml_Edge> vml_edges;




    private vml_EdgeStyle vml_edgestyle;




    private vml_Edge vml_edge;




    private vml_Edge vml_edge;




    private vml_EdgeStyle vml_edgestyle;




    private List<vml_Edge> vml_edges;




    private vml_Graph vml_graph;


    public vml_Node(
        String title,        String icone    ) {
        super(
        );
        this.title = title;
        this.icone = icone;
        this.vml_edges = new ArrayList<>();
        this.vml_edges = new ArrayList<>();
    }

    public vml_Node(
        String title,        String icone        ArrayList<vml_Edge> vml_edges,        ArrayList<vml_Edge> vml_edges    ) {
        this.title = title;
        this.icone = icone;
        this.vml_edges = vml_edges;
        this.vml_edges = vml_edges;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getIcone() {
        return icone;
    }

    public void setIcone(String icone) {
        this.icone = icone;
    }

    public List<vml_Edge> getVml_edges() {
        return vml_edges;
    }

    public void addVml_edge(Vml_edge vml_edge) {
        this.vml_edges.add(vml_edge);
    }
    public vml_EdgeStyle getVml_edgestyle() {
        return vml_edgestyle;
    }

    public void setVml_edgestyle(vml_EdgeStyle vml_edgestyle) {
        this.vml_edgestyle = vml_edgestyle;
    }
    public vml_Edge getVml_edge() {
        return vml_edge;
    }

    public void setVml_edge(vml_Edge vml_edge) {
        this.vml_edge = vml_edge;
    }
    public vml_Edge getVml_edge() {
        return vml_edge;
    }

    public void setVml_edge(vml_Edge vml_edge) {
        this.vml_edge = vml_edge;
    }
    public vml_EdgeStyle getVml_edgestyle() {
        return vml_edgestyle;
    }

    public void setVml_edgestyle(vml_EdgeStyle vml_edgestyle) {
        this.vml_edgestyle = vml_edgestyle;
    }
    public List<vml_Edge> getVml_edges() {
        return vml_edges;
    }

    public void addVml_edge(Vml_edge vml_edge) {
        this.vml_edges.add(vml_edge);
    }
    public vml_Graph getVml_graph() {
        return vml_graph;
    }

    public void setVml_graph(vml_Graph vml_graph) {
        this.vml_graph = vml_graph;
    }

}