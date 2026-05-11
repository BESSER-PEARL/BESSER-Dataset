





import java.util.List;
import java.util.ArrayList;

public class diagram_style_WorkspaceImageDescription extends style_ContainerStyleDescription, style_NodeStyleDescription {

    private String workspacePath;



    public diagram_style_WorkspaceImageDescription(
        String workspacePath    ) {
        super(
        );
        this.workspacePath = workspacePath;
    }


    public String getWorkspacepath() {
        return workspacePath;
    }

    public void setWorkspacepath(String workspacePath) {
        this.workspacePath = workspacePath;
    }


}