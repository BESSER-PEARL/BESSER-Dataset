





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_EdgeCreationDescription extends MappingBasedToolDescription {

    private String iconPath;
    private String connectionStartPrecondition;



    public viewpoint_tool_EdgeCreationDescription(
        String iconPath,        String connectionStartPrecondition    ) {
        super(
        );
        this.iconPath = iconPath;
        this.connectionStartPrecondition = connectionStartPrecondition;
    }


    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
    }
    public String getConnectionstartprecondition() {
        return connectionStartPrecondition;
    }

    public void setConnectionstartprecondition(String connectionStartPrecondition) {
        this.connectionStartPrecondition = connectionStartPrecondition;
    }


}