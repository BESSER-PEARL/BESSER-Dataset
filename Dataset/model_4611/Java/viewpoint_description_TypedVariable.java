





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_TypedVariable extends description_SubVariable, description_InteractiveVariableDescription {

    private String defaultValueExpression;



    public viewpoint_description_TypedVariable(
        String defaultValueExpression    ) {
        super(
        );
        this.defaultValueExpression = defaultValueExpression;
    }


    public String getDefaultvalueexpression() {
        return defaultValueExpression;
    }

    public void setDefaultvalueexpression(String defaultValueExpression) {
        this.defaultValueExpression = defaultValueExpression;
    }


}