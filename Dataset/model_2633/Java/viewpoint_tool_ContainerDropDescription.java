





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_ContainerDropDescription extends MappingBasedToolDescription {

    private String dragSource;
    private boolean moveEdges;





    private tool_ElementDropVariable tool_elementdropvariable;


    public viewpoint_tool_ContainerDropDescription(
        String dragSource,        boolean moveEdges    ) {
        super(
        );
        this.dragSource = dragSource;
        this.moveEdges = moveEdges;
    }


    public String getDragsource() {
        return dragSource;
    }

    public void setDragsource(String dragSource) {
        this.dragSource = dragSource;
    }
    public boolean getMoveedges() {
        return moveEdges;
    }

    public void setMoveedges(boolean moveEdges) {
        this.moveEdges = moveEdges;
    }

    public tool_ElementDropVariable getTool_elementdropvariable() {
        return tool_elementdropvariable;
    }

    public void setTool_elementdropvariable(tool_ElementDropVariable tool_elementdropvariable) {
        this.tool_elementdropvariable = tool_elementdropvariable;
    }

}