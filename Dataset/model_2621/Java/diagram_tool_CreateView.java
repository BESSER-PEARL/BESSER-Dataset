





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_CreateView extends ContainerModelOperation {

    private String variableName;
    private String containerViewExpression;





    private DiagramElementMapping diagramelementmapping;


    public diagram_tool_CreateView(
        String variableName,        String containerViewExpression    ) {
        super(
        );
        this.variableName = variableName;
        this.containerViewExpression = containerViewExpression;
    }


    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }
    public String getContainerviewexpression() {
        return containerViewExpression;
    }

    public void setContainerviewexpression(String containerViewExpression) {
        this.containerViewExpression = containerViewExpression;
    }

    public DiagramElementMapping getDiagramelementmapping() {
        return diagramelementmapping;
    }

    public void setDiagramelementmapping(DiagramElementMapping diagramelementmapping) {
        this.diagramelementmapping = diagramelementmapping;
    }

}