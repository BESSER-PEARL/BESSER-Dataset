





import java.util.List;
import java.util.ArrayList;

public class notation_View extends EModelElement, ecore_EClass {

    private String type;
    private boolean visible;
    private boolean mutable;





    private List<notation_Node> notation_nodes;




    private notation_Edge notation_edge;




    private notation_Edge notation_edge;




    private notation_Diagram notation_diagram;




    private List<notation_Edge> notation_edges;




    private List<notation_Edge> notation_edges;




    private List<notation_Node> notation_nodes;


    public notation_View(
        String type,        boolean visible,        boolean mutable    ) {
        super(
        );
        this.type = type;
        this.visible = visible;
        this.mutable = mutable;
        this.notation_nodes = new ArrayList<>();
        this.notation_edges = new ArrayList<>();
        this.notation_edges = new ArrayList<>();
        this.notation_nodes = new ArrayList<>();
    }

    public notation_View(
        String type,        boolean visible,        boolean mutable        ArrayList<notation_Node> notation_nodes,        ArrayList<notation_Edge> notation_edges,        ArrayList<notation_Edge> notation_edges,        ArrayList<notation_Node> notation_nodes    ) {
        this.type = type;
        this.visible = visible;
        this.mutable = mutable;
        this.notation_nodes = notation_nodes;
        this.notation_edges = notation_edges;
        this.notation_edges = notation_edges;
        this.notation_nodes = notation_nodes;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
    public notation_Diagram getNotation_diagram() {
        return notation_diagram;
    }

    public void setNotation_diagram(notation_Diagram notation_diagram) {
        this.notation_diagram = notation_diagram;
    }
    public List<notation_Edge> getNotation_edges() {
        return notation_edges;
    }

    public void addNotation_edge(Notation_edge notation_edge) {
        this.notation_edges.add(notation_edge);
    }
    public List<notation_Edge> getNotation_edges() {
        return notation_edges;
    }

    public void addNotation_edge(Notation_edge notation_edge) {
        this.notation_edges.add(notation_edge);
    }
    public List<notation_Node> getNotation_nodes() {
        return notation_nodes;
    }

    public void addNotation_node(Notation_node notation_node) {
        this.notation_nodes.add(notation_node);
    }

}