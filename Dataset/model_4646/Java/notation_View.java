





import java.util.List;
import java.util.ArrayList;

public class notation_View  {

    private boolean mutable;
    private String type;
    private boolean visible;





    private List<notation_Node> notation_nodes;




    private List<notation_Node> notation_nodes;




    private List<notation_Edge> notation_edges;




    private notation_Diagram notation_diagram;




    private List<notation_Edge> notation_edges;




    private notation_Edge notation_edge;




    private List<notation_Style> notation_styles;




    private notation_Edge notation_edge;


    public notation_View(
        boolean mutable,        String type,        boolean visible    ) {
        this.mutable = mutable;
        this.type = type;
        this.visible = visible;
        this.notation_nodes = new ArrayList<>();
        this.notation_nodes = new ArrayList<>();
        this.notation_edges = new ArrayList<>();
        this.notation_edges = new ArrayList<>();
        this.notation_styles = new ArrayList<>();
    }

    public notation_View(
        boolean mutable,        String type,        boolean visible        ArrayList<notation_Node> notation_nodes,        ArrayList<notation_Node> notation_nodes,        ArrayList<notation_Edge> notation_edges,        ArrayList<notation_Edge> notation_edges,        ArrayList<notation_Style> notation_styles    ) {
        this.mutable = mutable;
        this.type = type;
        this.visible = visible;
        this.notation_nodes = notation_nodes;
        this.notation_nodes = notation_nodes;
        this.notation_edges = notation_edges;
        this.notation_edges = notation_edges;
        this.notation_styles = notation_styles;
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
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
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
    public List<notation_Edge> getNotation_edges() {
        return notation_edges;
    }

    public void addNotation_edge(Notation_edge notation_edge) {
        this.notation_edges.add(notation_edge);
    }
    public notation_Edge getNotation_edge() {
        return notation_edge;
    }

    public void setNotation_edge(notation_Edge notation_edge) {
        this.notation_edge = notation_edge;
    }
    public List<notation_Style> getNotation_styles() {
        return notation_styles;
    }

    public void addNotation_style(Notation_style notation_style) {
        this.notation_styles.add(notation_style);
    }
    public notation_Edge getNotation_edge() {
        return notation_edge;
    }

    public void setNotation_edge(notation_Edge notation_edge) {
        this.notation_edge = notation_edge;
    }

}