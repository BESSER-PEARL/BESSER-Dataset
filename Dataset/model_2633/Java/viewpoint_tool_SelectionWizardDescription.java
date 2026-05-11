





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_SelectionWizardDescription extends tool_AbstractToolDescription, description_SelectionDescription {

    private String iconPath;
    private String windowImagePath;
    private String windowTitle;





    private tool_InitialOperation tool_initialoperation;


    public viewpoint_tool_SelectionWizardDescription(
        String iconPath,        String windowImagePath,        String windowTitle    ) {
        super(
        );
        this.iconPath = iconPath;
        this.windowImagePath = windowImagePath;
        this.windowTitle = windowTitle;
    }


    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
    }
    public String getWindowimagepath() {
        return windowImagePath;
    }

    public void setWindowimagepath(String windowImagePath) {
        this.windowImagePath = windowImagePath;
    }
    public String getWindowtitle() {
        return windowTitle;
    }

    public void setWindowtitle(String windowTitle) {
        this.windowTitle = windowTitle;
    }

    public tool_InitialOperation getTool_initialoperation() {
        return tool_initialoperation;
    }

    public void setTool_initialoperation(tool_InitialOperation tool_initialoperation) {
        this.tool_initialoperation = tool_initialoperation;
    }

}