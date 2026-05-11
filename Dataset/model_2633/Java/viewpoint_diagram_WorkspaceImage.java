





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_WorkspaceImage extends diagram_ContainerStyle, diagram_NodeStyle {

    private String workspacePath;



    public viewpoint_diagram_WorkspaceImage(
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