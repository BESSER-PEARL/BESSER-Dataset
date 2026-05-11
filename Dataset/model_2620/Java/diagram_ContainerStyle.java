





import java.util.List;
import java.util.ArrayList;

public class diagram_ContainerStyle extends HideLabelCapabilityStyle, BorderedStyle, LabelStyle, Style {

    private String containerLabelDirection;





    private diagram_DDiagramElementContainer diagram_ddiagramelementcontainer;


    public diagram_ContainerStyle(
        String containerLabelDirection    ) {
        super(
        );
        this.containerLabelDirection = containerLabelDirection;
    }


    public String getContainerlabeldirection() {
        return containerLabelDirection;
    }

    public void setContainerlabeldirection(String containerLabelDirection) {
        this.containerLabelDirection = containerLabelDirection;
    }

    public diagram_DDiagramElementContainer getDiagram_ddiagramelementcontainer() {
        return diagram_ddiagramelementcontainer;
    }

    public void setDiagram_ddiagramelementcontainer(diagram_DDiagramElementContainer diagram_ddiagramelementcontainer) {
        this.diagram_ddiagramelementcontainer = diagram_ddiagramelementcontainer;
    }

}