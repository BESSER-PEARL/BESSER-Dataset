





import java.util.List;
import java.util.ArrayList;

public class model_DoorsFolder extends DoorsTreeNode {

    private boolean project;



    public model_DoorsFolder(
        boolean project    ) {
        super(
        );
        this.project = project;
    }


    public boolean getProject() {
        return project;
    }

    public void setProject(boolean project) {
        this.project = project;
    }


}