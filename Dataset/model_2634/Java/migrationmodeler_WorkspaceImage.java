





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_WorkspaceImage extends NodeStyle, ContainerStyle {

    private String workspacePath;



    public migrationmodeler_WorkspaceImage(
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