





import java.util.List;
import java.util.ArrayList;

public class query_SingleExpressionWhereEntry extends ExpressionWhereEntry {

    private String operator;



    public query_SingleExpressionWhereEntry(
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