





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_ToolDescription extends MappingBasedToolDescription {

    private String iconPath;



    public viewpoint_tool_ToolDescription(
        String iconPath    ) {
        super(
        );
        this.iconPath = iconPath;
    }


    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
    }


}