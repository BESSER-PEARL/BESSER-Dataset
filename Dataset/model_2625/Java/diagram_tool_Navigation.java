





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_Navigation extends ContainerModelOperation {

    private boolean createIfNotExistent;





    private DiagramDescription diagramdescription;


    public diagram_tool_Navigation(
        boolean createIfNotExistent    ) {
        super(
        );
        this.createIfNotExistent = createIfNotExistent;
    }


    public boolean getCreateifnotexistent() {
        return createIfNotExistent;
    }

    public void setCreateifnotexistent(boolean createIfNotExistent) {
        this.createIfNotExistent = createIfNotExistent;
    }

    public DiagramDescription getDiagramdescription() {
        return diagramdescription;
    }

    public void setDiagramdescription(DiagramDescription diagramdescription) {
        this.diagramdescription = diagramdescription;
    }

}