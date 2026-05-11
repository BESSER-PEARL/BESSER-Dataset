





import java.util.List;
import java.util.ArrayList;

public class notation_View extends NotationElement {

    private String viewType;
    private String viewDetails;





    private List<notation_Node> notation_nodes;




    private notation_Edge notation_edge;




    private notation_EObject notation_eobject;




    private notation_Edge notation_edge;




    private List<notation_Edge> notation_edges;




    private List<notation_Edge> notation_edges;


    public notation_View(
        String viewType,        String viewDetails    ) {
        super(
        );
        this.viewType = viewType;
        this.viewDetails = viewDetails;
        this.notation_nodes = new ArrayList<>();
        this.notation_edges = new ArrayList<>();
        this.notation_edges = new ArrayList<>();
    }

    public notation_View(
        String viewType,        String viewDetails        ArrayList<notation_Node> notation_nodes,        ArrayList<notation_Edge> notation_edges,        ArrayList<notation_Edge> notation_edges    ) {
        this.viewType = viewType;
        this.viewDetails = viewDetails;
        this.notation_nodes = notation_nodes;
        this.notation_edges = notation_edges;
        this.notation_edges = notation_edges;
    }

    public String getViewtype() {
        return viewType;
    }

    public void setViewtype(String viewType) {
        this.viewType = viewType;
    }
    public String getViewdetails() {
        return viewDetails;
    }

    public void setViewdetails(String viewDetails) {
        this.viewDetails = viewDetails;
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
    public notation_EObject getNotation_eobject() {
        return notation_eobject;
    }

    public void setNotation_eobject(notation_EObject notation_eobject) {
        this.notation_eobject = notation_eobject;
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
    public List<notation_Edge> getNotation_edges() {
        return notation_edges;
    }

    public void addNotation_edge(Notation_edge notation_edge) {
        this.notation_edges.add(notation_edge);
    }

}