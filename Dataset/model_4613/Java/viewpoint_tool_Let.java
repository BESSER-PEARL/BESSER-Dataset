





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_Let extends ContainerModelOperation {

    private String variableName;
    private String valueExpression;



    public viewpoint_tool_Let(
        String variableName,        String valueExpression    ) {
        super(
        );
        this.variableName = variableName;
        this.valueExpression = valueExpression;
    }


    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }
    public String getValueexpression() {
        return valueExpression;
    }

    public void setValueexpression(String valueExpression) {
        this.valueExpression = valueExpression;
    }


}