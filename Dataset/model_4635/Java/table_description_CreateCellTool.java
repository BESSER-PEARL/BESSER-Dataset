





import java.util.List;
import java.util.ArrayList;

public class table_description_CreateCellTool extends description_TableTool, tool_AbstractToolDescription {






    private tool_EditMaskVariables tool_editmaskvariables;




    private IntersectionMapping intersectionmapping;


    public table_description_CreateCellTool(
    ) {
        super(
        );
    }



    public tool_EditMaskVariables getTool_editmaskvariables() {
        return tool_editmaskvariables;
    }

    public void setTool_editmaskvariables(tool_EditMaskVariables tool_editmaskvariables) {
        this.tool_editmaskvariables = tool_editmaskvariables;
    }
    public IntersectionMapping getIntersectionmapping() {
        return intersectionmapping;
    }

    public void setIntersectionmapping(IntersectionMapping intersectionmapping) {
        this.intersectionmapping = intersectionmapping;
    }

}