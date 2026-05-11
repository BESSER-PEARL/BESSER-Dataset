





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_ToolDescription extends MappingBasedToolDescription {

    private String iconPath;





    private tool_InitialOperation tool_initialoperation;




    private tool_ElementViewVariable tool_elementviewvariable;


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

    public tool_InitialOperation getTool_initialoperation() {
        return tool_initialoperation;
    }

    public void setTool_initialoperation(tool_InitialOperation tool_initialoperation) {
        this.tool_initialoperation = tool_initialoperation;
    }
    public tool_ElementViewVariable getTool_elementviewvariable() {
        return tool_elementviewvariable;
    }

    public void setTool_elementviewvariable(tool_ElementViewVariable tool_elementviewvariable) {
        this.tool_elementviewvariable = tool_elementviewvariable;
    }

}