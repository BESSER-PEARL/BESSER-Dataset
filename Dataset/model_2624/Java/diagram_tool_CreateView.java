





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_CreateView extends ContainerModelOperation {

    private String containerViewExpression;
    private String variableName;





    private DiagramElementMapping diagramelementmapping;


    public diagram_tool_CreateView(
        String containerViewExpression,        String variableName    ) {
        super(
        );
        this.containerViewExpression = containerViewExpression;
        this.variableName = variableName;
    }


    public String getContainerviewexpression() {
        return containerViewExpression;
    }

    public void setContainerviewexpression(String containerViewExpression) {
        this.containerViewExpression = containerViewExpression;
    }
    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }

    public DiagramElementMapping getDiagramelementmapping() {
        return diagramelementmapping;
    }

    public void setDiagramelementmapping(DiagramElementMapping diagramelementmapping) {
        this.diagramelementmapping = diagramelementmapping;
    }

}