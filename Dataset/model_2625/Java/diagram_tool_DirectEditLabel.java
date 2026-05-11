





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_DirectEditLabel extends MappingBasedToolDescription {

    private String inputLabelExpression;



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


}