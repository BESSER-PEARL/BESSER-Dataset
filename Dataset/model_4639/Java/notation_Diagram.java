





import java.util.List;
import java.util.ArrayList;

public class notation_Diagram extends View {

    private String measurementUnit;
    private String name;





    private List<notation_Edge> notation_edges;




    private notation_MultiDiagramLinkStyle notation_multidiagramlinkstyle;




    private notation_DiagramLinkStyle notation_diagramlinkstyle;




    private List<notation_Edge> notation_edges;


    public notation_Diagram(
        String measurementUnit,        String name    ) {
        super(
        );
        this.measurementUnit = measurementUnit;
        this.name = name;
        this.notation_edges = new ArrayList<>();
        this.notation_edges = new ArrayList<>();
    }

    public notation_Diagram(
        String measurementUnit,        String name        ArrayList<notation_Edge> notation_edges,        ArrayList<notation_Edge> notation_edges    ) {
        this.measurementUnit = measurementUnit;
        this.name = name;
        this.notation_edges = notation_edges;
        this.notation_edges = notation_edges;
    }

    public String getMeasurementunit() {
        return measurementUnit;
    }

    public void setMeasurementunit(String measurementUnit) {
        this.measurementUnit = measurementUnit;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<notation_Edge> getNotation_edges() {
        return notation_edges;
    }

    public void addNotation_edge(Notation_edge notation_edge) {
        this.notation_edges.add(notation_edge);
    }
    public notation_MultiDiagramLinkStyle getNotation_multidiagramlinkstyle() {
        return notation_multidiagramlinkstyle;
    }

    public void setNotation_multidiagramlinkstyle(notation_MultiDiagramLinkStyle notation_multidiagramlinkstyle) {
        this.notation_multidiagramlinkstyle = notation_multidiagramlinkstyle;
    }
    public notation_DiagramLinkStyle getNotation_diagramlinkstyle() {
        return notation_diagramlinkstyle;
    }

    public void setNotation_diagramlinkstyle(notation_DiagramLinkStyle notation_diagramlinkstyle) {
        this.notation_diagramlinkstyle = notation_diagramlinkstyle;
    }
    public List<notation_Edge> getNotation_edges() {
        return notation_edges;
    }

    public void addNotation_edge(Notation_edge notation_edge) {
        this.notation_edges.add(notation_edge);
    }

}