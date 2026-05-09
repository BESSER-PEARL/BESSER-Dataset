





import java.util.List;
import java.util.ArrayList;

public class ptnet_Variable  {

    private String name;





    private ptnet_VariableExpression ptnet_variableexpression;




    private ptnet_VariableValues ptnet_variablevalues;


    public ptnet_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ptnet_VariableExpression getPtnet_variableexpression() {
        return ptnet_variableexpression;
    }

    public void setPtnet_variableexpression(ptnet_VariableExpression ptnet_variableexpression) {
        this.ptnet_variableexpression = ptnet_variableexpression;
    }
    public ptnet_VariableValues getPtnet_variablevalues() {
        return ptnet_variablevalues;
    }

    public void setPtnet_variablevalues(ptnet_VariableValues ptnet_variablevalues) {
        this.ptnet_variablevalues = ptnet_variablevalues;
    }

}