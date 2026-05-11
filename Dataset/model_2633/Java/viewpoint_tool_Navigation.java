





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_Navigation extends ContainerModelOperation {

    private boolean createIfNotExistent;



    public viewpoint_tool_Navigation(
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


}