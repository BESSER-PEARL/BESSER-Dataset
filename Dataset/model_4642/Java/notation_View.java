





import java.util.List;
import java.util.ArrayList;

public class notation_View extends EModelElement {

    private boolean visible;
    private boolean mutable;
    private String type;





    private List<notation_Edge> notation_edges;




    private notation_Diagram notation_diagram;




    private List<notation_Node> notation_nodes;




    private List<notation_Node> notation_nodes;




    private notation_Edge notation_edge;




    private notation_Edge notation_edge;




    private List<notation_Edge> notation_edges;


    public notation_View(
        boolean visible,        boolean mutable,        String type    ) {
        super(
        );
        this.visible = visible;
        this.mutable = mutable;
        this.type = type;
        this.notation_edges = new ArrayList<>();
        this.notation_nodes = new ArrayList<>();
        this.notation_nodes = new ArrayList<>();
        this.notation_edges = new ArrayList<>();
    }

    public notation_View(
        boolean visible,        boolean mutable,        String type        ArrayList<notation_Edge> notation_edges,        ArrayList<notation_Node> notation_nodes,        ArrayList<notation_Node> notation_nodes,        ArrayList<notation_Edge> notation_edges    ) {
        this.visible = visible;
        this.mutable = mutable;
        this.type = type;
        this.notation_edges = notation_edges;
        this.notation_nodes = notation_nodes;
        this.notation_nodes = notation_nodes;
        this.notation_edges = notation_edges;
    }

    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }
    public boolean getMutable() {
        return mutable;
    }

    public void setMutable(boolean mutable) {
        this.mutable = mutable;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<notation_Edge> getNotation_edges() {
        return notation_edges;
    }

    public void addNotation_edge(Notation_edge notation_edge) {
        this.notation_edges.add(notation_edge);
    }
    public notation_Diagram getNotation_diagram() {
        return notation_diagram;
    }

    public void setNotation_diagram(notation_Diagram notation_diagram) {
        this.notation_diagram = notation_diagram;
    }
    public List<notation_Node> getNotation_nodes() {
        return notation_nodes;
    }

    public void addNotation_node(Notation_node notation_node) {
        this.notation_nodes.add(notation_node);
    }
    public List<notation_Node> getNotation_nodes() {
        return notation_nodes;
    }

    public void addNotation_node(Notation_node notation_node) {
        this.notation_nodes.add(notation_node);
    }
    public notation_Edge getNotation_edge() {
        return notation_edge;
    }

    public void setNotation_edge(notation_Edge notation_edge) {
        this.notation_edge = notation_edge;
    }
    public notation_Edge getNotation_edge() {
        return notation_edge;
    }

    public void setNotation_edge(notation_Edge notation_edge) {
        this.notation_edge = notation_edge;
    }
    public List<notation_Edge> getNotation_edges() {
        return notation_edges;
    }

    public void addNotation_edge(Notation_edge notation_edge) {
        this.notation_edges.add(notation_edge);
    }

}