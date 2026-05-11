





import java.util.List;
import java.util.ArrayList;

public class diagram_GaugeCompositeStyle extends NodeStyle {

    private String alignment;





    private List<diagram_GaugeSection> diagram_gaugesections;


    public diagram_GaugeCompositeStyle(
        String alignment    ) {
        super(
        );
        this.alignment = alignment;
        this.diagram_gaugesections = new ArrayList<>();
    }

    public diagram_GaugeCompositeStyle(
        String alignment        ArrayList<diagram_GaugeSection> diagram_gaugesections    ) {
        this.alignment = alignment;
        this.diagram_gaugesections = diagram_gaugesections;
    }

    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }

    public List<diagram_GaugeSection> getDiagram_gaugesections() {
        return diagram_gaugesections;
    }

    public void addDiagram_gaugesection(Diagram_gaugesection diagram_gaugesection) {
        this.diagram_gaugesections.add(diagram_gaugesection);
    }

}