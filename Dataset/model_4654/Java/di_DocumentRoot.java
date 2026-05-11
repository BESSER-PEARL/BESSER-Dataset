





import java.util.List;
import java.util.ArrayList;

public class di_DocumentRoot  {

    private String mixed;





    private List<di_DiagramElement> di_diagramelements;




    private List<di_Shape> di_shapes;




    private List<di_Edge> di_edges;




    private List<di_Node> di_nodes;




    private List<di_Style> di_styles;




    private List<di_Plane> di_planes;




    private List<di_Diagram> di_diagrams;




    private List<di_Label> di_labels;


    public di_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.di_diagramelements = new ArrayList<>();
        this.di_shapes = new ArrayList<>();
        this.di_edges = new ArrayList<>();
        this.di_nodes = new ArrayList<>();
        this.di_styles = new ArrayList<>();
        this.di_planes = new ArrayList<>();
        this.di_diagrams = new ArrayList<>();
        this.di_labels = new ArrayList<>();
    }

    public di_DocumentRoot(
        String mixed        ArrayList<di_DiagramElement> di_diagramelements,        ArrayList<di_Shape> di_shapes,        ArrayList<di_Edge> di_edges,        ArrayList<di_Node> di_nodes,        ArrayList<di_Style> di_styles,        ArrayList<di_Plane> di_planes,        ArrayList<di_Diagram> di_diagrams,        ArrayList<di_Label> di_labels    ) {
        this.mixed = mixed;
        this.di_diagramelements = di_diagramelements;
        this.di_shapes = di_shapes;
        this.di_edges = di_edges;
        this.di_nodes = di_nodes;
        this.di_styles = di_styles;
        this.di_planes = di_planes;
        this.di_diagrams = di_diagrams;
        this.di_labels = di_labels;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<di_DiagramElement> getDi_diagramelements() {
        return di_diagramelements;
    }

    public void addDi_diagramelement(Di_diagramelement di_diagramelement) {
        this.di_diagramelements.add(di_diagramelement);
    }
    public List<di_Shape> getDi_shapes() {
        return di_shapes;
    }

    public void addDi_shape(Di_shape di_shape) {
        this.di_shapes.add(di_shape);
    }
    public List<di_Edge> getDi_edges() {
        return di_edges;
    }

    public void addDi_edge(Di_edge di_edge) {
        this.di_edges.add(di_edge);
    }
    public List<di_Node> getDi_nodes() {
        return di_nodes;
    }

    public void addDi_node(Di_node di_node) {
        this.di_nodes.add(di_node);
    }
    public List<di_Style> getDi_styles() {
        return di_styles;
    }

    public void addDi_style(Di_style di_style) {
        this.di_styles.add(di_style);
    }
    public List<di_Plane> getDi_planes() {
        return di_planes;
    }

    public void addDi_plane(Di_plane di_plane) {
        this.di_planes.add(di_plane);
    }
    public List<di_Diagram> getDi_diagrams() {
        return di_diagrams;
    }

    public void addDi_diagram(Di_diagram di_diagram) {
        this.di_diagrams.add(di_diagram);
    }
    public List<di_Label> getDi_labels() {
        return di_labels;
    }

    public void addDi_label(Di_label di_label) {
        this.di_labels.add(di_label);
    }

}