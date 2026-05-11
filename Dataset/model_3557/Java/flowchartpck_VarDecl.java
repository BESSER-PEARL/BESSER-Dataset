





import java.util.List;
import java.util.ArrayList;

public class flowchartpck_VarDecl extends Statement {

    private String key;





    private flowchartpck_Expression flowchartpck_expression;




    private flowchartpck_Assignation flowchartpck_assignation;


    public flowchartpck_VarDecl(
        String key    ) {
        super(
        );
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public flowchartpck_Expression getFlowchartpck_expression() {
        return flowchartpck_expression;
    }

    public void setFlowchartpck_expression(flowchartpck_Expression flowchartpck_expression) {
        this.flowchartpck_expression = flowchartpck_expression;
    }
    public flowchartpck_Assignation getFlowchartpck_assignation() {
        return flowchartpck_assignation;
    }

    public void setFlowchartpck_assignation(flowchartpck_Assignation flowchartpck_assignation) {
        this.flowchartpck_assignation = flowchartpck_assignation;
    }

}