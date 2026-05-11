





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_CreateView extends ContainerModelOperation {

    private String variableName;
    private String containerViewExpression;





    private description_DiagramElementMapping description_diagramelementmapping;


    public viewpoint_tool_CreateView(
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

    public description_DiagramElementMapping getDescription_diagramelementmapping() {
        return description_diagramelementmapping;
    }

    public void setDescription_diagramelementmapping(description_DiagramElementMapping description_diagramelementmapping) {
        this.description_diagramelementmapping = description_diagramelementmapping;
    }

}