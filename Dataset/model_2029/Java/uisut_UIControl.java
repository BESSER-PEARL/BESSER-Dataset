





import java.util.List;
import java.util.ArrayList;

public class uisut_UIControl extends UISUTElement {

    private String variableName;
    private String valueExpression;



    public uisut_UIControl(
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