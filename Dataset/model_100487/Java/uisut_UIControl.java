





import java.util.List;
import java.util.ArrayList;

public class uisut_UIControl extends UISUTElement {

    private String valueExpression;
    private String variableName;



    public uisut_UIControl(
        String valueExpression,        String variableName    ) {
        super(
        );
        this.valueExpression = valueExpression;
        this.variableName = variableName;
    }


    public String getValueexpression() {
        return valueExpression;
    }

    public void setValueexpression(String valueExpression) {
        this.valueExpression = valueExpression;
    }
    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }


}