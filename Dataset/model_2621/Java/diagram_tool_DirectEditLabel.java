





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_DirectEditLabel extends MappingBasedToolDescription {

    private String inputLabelExpression;





    private tool_InitialOperation tool_initialoperation;


    public diagram_tool_DirectEditLabel(
        String inputLabelExpression    ) {
        super(
        );
        this.inputLabelExpression = inputLabelExpression;
    }


    public String getInputlabelexpression() {
        return inputLabelExpression;
    }

    public void setInputlabelexpression(String inputLabelExpression) {
        this.inputLabelExpression = inputLabelExpression;
    }

    public tool_InitialOperation getTool_initialoperation() {
        return tool_initialoperation;
    }

    public void setTool_initialoperation(tool_InitialOperation tool_initialoperation) {
        this.tool_initialoperation = tool_initialoperation;
    }

}