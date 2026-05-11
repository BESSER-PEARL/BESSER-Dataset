





import java.util.List;
import java.util.ArrayList;

public class notation_MultiDiagramLinkStyle extends Style {






    private List<notation_Diagram> notation_diagrams;


    public notation_MultiDiagramLinkStyle(
    ) {
        super(
        );
        this.notation_diagrams = new ArrayList<>();
    }

    public notation_MultiDiagramLinkStyle(
        ArrayList<notation_Diagram> notation_diagrams    ) {
        this.notation_diagrams = notation_diagrams;
    }


    public List<notation_Diagram> getNotation_diagrams() {
        return notation_diagrams;
    }

    public void addNotation_diagram(Notation_diagram notation_diagram) {
        this.notation_diagrams.add(notation_diagram);
    }

}