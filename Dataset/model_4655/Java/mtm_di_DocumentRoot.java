





import java.util.List;
import java.util.ArrayList;

public class mtm_di_DocumentRoot  {

    private String mixed;





    private List<mtm_di_Edge> mtm_di_edges;




    private List<mtm_di_Style> mtm_di_styles;




    private List<mtm_di_Diagram> mtm_di_diagrams;




    private List<mtm_di_DiagramElement> mtm_di_diagramelements;




    private List<mtm_di_LabeledShape> mtm_di_labeledshapes;




    private List<mtm_di_LabeledEdge> mtm_di_labelededges;




    private List<mtm_di_Plane> mtm_di_planes;




    private List<mtm_di_Node> mtm_di_nodes;




    private List<mtm_di_Shape> mtm_di_shapes;




    private List<mtm_di_Label> mtm_di_labels;


    public mtm_di_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.mtm_di_edges = new ArrayList<>();
        this.mtm_di_styles = new ArrayList<>();
        this.mtm_di_diagrams = new ArrayList<>();
        this.mtm_di_diagramelements = new ArrayList<>();
        this.mtm_di_labeledshapes = new ArrayList<>();
        this.mtm_di_labelededges = new ArrayList<>();
        this.mtm_di_planes = new ArrayList<>();
        this.mtm_di_nodes = new ArrayList<>();
        this.mtm_di_shapes = new ArrayList<>();
        this.mtm_di_labels = new ArrayList<>();
    }

    public mtm_di_DocumentRoot(
        String mixed        ArrayList<mtm_di_Edge> mtm_di_edges,        ArrayList<mtm_di_Style> mtm_di_styles,        ArrayList<mtm_di_Diagram> mtm_di_diagrams,        ArrayList<mtm_di_DiagramElement> mtm_di_diagramelements,        ArrayList<mtm_di_LabeledShape> mtm_di_labeledshapes,        ArrayList<mtm_di_LabeledEdge> mtm_di_labelededges,        ArrayList<mtm_di_Plane> mtm_di_planes,        ArrayList<mtm_di_Node> mtm_di_nodes,        ArrayList<mtm_di_Shape> mtm_di_shapes,        ArrayList<mtm_di_Label> mtm_di_labels    ) {
        this.mixed = mixed;
        this.mtm_di_edges = mtm_di_edges;
        this.mtm_di_styles = mtm_di_styles;
        this.mtm_di_diagrams = mtm_di_diagrams;
        this.mtm_di_diagramelements = mtm_di_diagramelements;
        this.mtm_di_labeledshapes = mtm_di_labeledshapes;
        this.mtm_di_labelededges = mtm_di_labelededges;
        this.mtm_di_planes = mtm_di_planes;
        this.mtm_di_nodes = mtm_di_nodes;
        this.mtm_di_shapes = mtm_di_shapes;
        this.mtm_di_labels = mtm_di_labels;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<mtm_di_Edge> getMtm_di_edges() {
        return mtm_di_edges;
    }

    public void addMtm_di_edge(Mtm_di_edge mtm_di_edge) {
        this.mtm_di_edges.add(mtm_di_edge);
    }
    public List<mtm_di_Style> getMtm_di_styles() {
        return mtm_di_styles;
    }

    public void addMtm_di_style(Mtm_di_style mtm_di_style) {
        this.mtm_di_styles.add(mtm_di_style);
    }
    public List<mtm_di_Diagram> getMtm_di_diagrams() {
        return mtm_di_diagrams;
    }

    public void addMtm_di_diagram(Mtm_di_diagram mtm_di_diagram) {
        this.mtm_di_diagrams.add(mtm_di_diagram);
    }
    public List<mtm_di_DiagramElement> getMtm_di_diagramelements() {
        return mtm_di_diagramelements;
    }

    public void addMtm_di_diagramelement(Mtm_di_diagramelement mtm_di_diagramelement) {
        this.mtm_di_diagramelements.add(mtm_di_diagramelement);
    }
    public List<mtm_di_LabeledShape> getMtm_di_labeledshapes() {
        return mtm_di_labeledshapes;
    }

    public void addMtm_di_labeledshape(Mtm_di_labeledshape mtm_di_labeledshape) {
        this.mtm_di_labeledshapes.add(mtm_di_labeledshape);
    }
    public List<mtm_di_LabeledEdge> getMtm_di_labelededges() {
        return mtm_di_labelededges;
    }

    public void addMtm_di_labelededge(Mtm_di_labelededge mtm_di_labelededge) {
        this.mtm_di_labelededges.add(mtm_di_labelededge);
    }
    public List<mtm_di_Plane> getMtm_di_planes() {
        return mtm_di_planes;
    }

    public void addMtm_di_plane(Mtm_di_plane mtm_di_plane) {
        this.mtm_di_planes.add(mtm_di_plane);
    }
    public List<mtm_di_Node> getMtm_di_nodes() {
        return mtm_di_nodes;
    }

    public void addMtm_di_node(Mtm_di_node mtm_di_node) {
        this.mtm_di_nodes.add(mtm_di_node);
    }
    public List<mtm_di_Shape> getMtm_di_shapes() {
        return mtm_di_shapes;
    }

    public void addMtm_di_shape(Mtm_di_shape mtm_di_shape) {
        this.mtm_di_shapes.add(mtm_di_shape);
    }
    public List<mtm_di_Label> getMtm_di_labels() {
        return mtm_di_labels;
    }

    public void addMtm_di_label(Mtm_di_label mtm_di_label) {
        this.mtm_di_labels.add(mtm_di_label);
    }

}