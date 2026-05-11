





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_SelectionWizardDescription extends description_SelectionDescription, tool_AbstractToolDescription {

    private String windowTitle;
    private String windowImagePath;
    private String iconPath;





    private tool_InitialOperation tool_initialoperation;




    private tool_ContainerViewVariable tool_containerviewvariable;


    public viewpoint_tool_SelectionWizardDescription(
        String windowTitle,        String windowImagePath,        String iconPath    ) {
        super(
        );
        this.windowTitle = windowTitle;
        this.windowImagePath = windowImagePath;
        this.iconPath = iconPath;
    }


    public String getWindowtitle() {
        return windowTitle;
    }

    public void setWindowtitle(String windowTitle) {
        this.windowTitle = windowTitle;
    }
    public String getWindowimagepath() {
        return windowImagePath;
    }

    public void setWindowimagepath(String windowImagePath) {
        this.windowImagePath = windowImagePath;
    }
    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
    }

    public tool_InitialOperation getTool_initialoperation() {
        return tool_initialoperation;
    }

    public void setTool_initialoperation(tool_InitialOperation tool_initialoperation) {
        this.tool_initialoperation = tool_initialoperation;
    }
    public tool_ContainerViewVariable getTool_containerviewvariable() {
        return tool_containerviewvariable;
    }

    public void setTool_containerviewvariable(tool_ContainerViewVariable tool_containerviewvariable) {
        this.tool_containerviewvariable = tool_containerviewvariable;
    }

}