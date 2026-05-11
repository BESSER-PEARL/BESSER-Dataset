





import java.util.List;
import java.util.ArrayList;

public class aredsl_Layer  {

    private String id;
    private String semantics;
    private String description;





    private aredsl_Editor aredsl_editor;




    private aredsl_TrackerAction aredsl_trackeraction;




    private List<aredsl_Edge> aredsl_edges;




    private List<aredsl_Node> aredsl_nodes;


    public aredsl_Layer(
        String id,        String semantics,        String description    ) {
        this.id = id;
        this.semantics = semantics;
        this.description = description;
        this.aredsl_edges = new ArrayList<>();
        this.aredsl_nodes = new ArrayList<>();
    }

    public aredsl_Layer(
        String id,        String semantics,        String description        ArrayList<aredsl_Edge> aredsl_edges,        ArrayList<aredsl_Node> aredsl_nodes    ) {
        this.id = id;
        this.semantics = semantics;
        this.description = description;
        this.aredsl_edges = aredsl_edges;
        this.aredsl_nodes = aredsl_nodes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSemantics() {
        return semantics;
    }

    public void setSemantics(String semantics) {
        this.semantics = semantics;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public aredsl_Editor getAredsl_editor() {
        return aredsl_editor;
    }

    public void setAredsl_editor(aredsl_Editor aredsl_editor) {
        this.aredsl_editor = aredsl_editor;
    }
    public aredsl_TrackerAction getAredsl_trackeraction() {
        return aredsl_trackeraction;
    }

    public void setAredsl_trackeraction(aredsl_TrackerAction aredsl_trackeraction) {
        this.aredsl_trackeraction = aredsl_trackeraction;
    }
    public List<aredsl_Edge> getAredsl_edges() {
        return aredsl_edges;
    }

    public void addAredsl_edge(Aredsl_edge aredsl_edge) {
        this.aredsl_edges.add(aredsl_edge);
    }
    public List<aredsl_Node> getAredsl_nodes() {
        return aredsl_nodes;
    }

    public void addAredsl_node(Aredsl_node aredsl_node) {
        this.aredsl_nodes.add(aredsl_node);
    }

}