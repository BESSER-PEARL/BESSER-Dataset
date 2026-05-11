





import java.util.List;
import java.util.ArrayList;

public class notation_Diagram extends View {

    private boolean showLocationForNewElementsDialog;
    private String locationForNewElements;
    private String name;





    private List<notation_Edge> notation_edges;


    public notation_Diagram(
        boolean showLocationForNewElementsDialog,        String locationForNewElements,        String name    ) {
        super(
        );
        this.showLocationForNewElementsDialog = showLocationForNewElementsDialog;
        this.locationForNewElements = locationForNewElements;
        this.name = name;
        this.notation_edges = new ArrayList<>();
    }

    public notation_Diagram(
        boolean showLocationForNewElementsDialog,        String locationForNewElements,        String name        ArrayList<notation_Edge> notation_edges    ) {
        this.showLocationForNewElementsDialog = showLocationForNewElementsDialog;
        this.locationForNewElements = locationForNewElements;
        this.name = name;
        this.notation_edges = notation_edges;
    }

    public boolean getShowlocationfornewelementsdialog() {
        return showLocationForNewElementsDialog;
    }

    public void setShowlocationfornewelementsdialog(boolean showLocationForNewElementsDialog) {
        this.showLocationForNewElementsDialog = showLocationForNewElementsDialog;
    }
    public String getLocationfornewelements() {
        return locationForNewElements;
    }

    public void setLocationfornewelements(String locationForNewElements) {
        this.locationForNewElements = locationForNewElements;
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

}