





import java.util.List;
import java.util.ArrayList;

public class model_ExistsContextualExpression extends Expression {

    private String contextId;





    private model_Expression model_expression;


    public model_ExistsContextualExpression(
        String contextId    ) {
        super(
        );
        this.contextId = contextId;
    }


    public String getContextid() {
        return contextId;
    }

    public void setContextid(String contextId) {
        this.contextId = contextId;
    }

    public model_Expression getModel_expression() {
        return model_expression;
    }

    public void setModel_expression(model_Expression model_expression) {
        this.model_expression = model_expression;
    }

}