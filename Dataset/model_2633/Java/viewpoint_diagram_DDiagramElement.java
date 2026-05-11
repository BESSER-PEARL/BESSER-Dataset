





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_DDiagramElement extends DNavigable, DRepresentationElement, DValidable {

    private String tooltipText;
    private boolean visible;





    private description_DiagramElementMapping description_diagramelementmapping;


    public viewpoint_diagram_DDiagramElement(
        String tooltipText,        boolean visible    ) {
        super(
        );
        this.tooltipText = tooltipText;
        this.visible = visible;
    }


    public String getTooltiptext() {
        return tooltipText;
    }

    public void setTooltiptext(String tooltipText) {
        this.tooltipText = tooltipText;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }

    public description_DiagramElementMapping getDescription_diagramelementmapping() {
        return description_diagramelementmapping;
    }

    public void setDescription_diagramelementmapping(description_DiagramElementMapping description_diagramelementmapping) {
        this.description_diagramelementmapping = description_diagramelementmapping;
    }

}