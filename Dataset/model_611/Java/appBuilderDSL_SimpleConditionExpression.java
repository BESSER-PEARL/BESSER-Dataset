





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_SimpleConditionExpression extends ConditionExpression {

    private String variableName;



    public appBuilderDSL_SimpleConditionExpression(
        String variableName    ) {
        super(
        );
        this.variableName = variableName;
    }


    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }


}