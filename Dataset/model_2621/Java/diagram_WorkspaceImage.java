





import java.util.List;
import java.util.ArrayList;

public class diagram_WorkspaceImage extends NodeStyle, ContainerStyle {

    private String workspacePath;



    public diagram_WorkspaceImage(
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