





import java.util.List;
import java.util.ArrayList;

public class model_expression_Operation extends IExpressionTerm {

    private String operator;



    public model_expression_Operation(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }


}