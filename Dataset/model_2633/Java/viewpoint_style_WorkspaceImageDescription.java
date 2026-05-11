





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_WorkspaceImageDescription extends style_NodeStyleDescription, style_ContainerStyleDescription {

    private String workspacePath;



    public viewpoint_style_WorkspaceImageDescription(
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