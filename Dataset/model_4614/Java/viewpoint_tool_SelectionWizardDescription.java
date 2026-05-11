





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_SelectionWizardDescription extends tool_AbstractToolDescription, description_SelectionDescription {

    private String windowTitle;
    private String iconPath;
    private String windowImagePath;





    private tool_InitialOperation tool_initialoperation;


    public viewpoint_tool_SelectionWizardDescription(
        String windowTitle,        String iconPath,        String windowImagePath    ) {
        super(
        );
        this.windowTitle = windowTitle;
        this.iconPath = iconPath;
        this.windowImagePath = windowImagePath;
    }


    public String getWindowtitle() {
        return windowTitle;
    }

    public void setWindowtitle(String windowTitle) {
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

    public tool_InitialOperation getTool_initialoperation() {
        return tool_initialoperation;
    }

    public void setTool_initialoperation(tool_InitialOperation tool_initialoperation) {
        this.tool_initialoperation = tool_initialoperation;
    }

}