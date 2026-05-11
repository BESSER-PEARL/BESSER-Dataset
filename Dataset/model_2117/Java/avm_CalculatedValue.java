





import java.util.List;
import java.util.ArrayList;

public class avm_CalculatedValue extends ValueExpressionType {

    private String Expression;
    private String Type;



    public avm_CalculatedValue(
        String Expression,        String Type    ) {
        super(
        );
        this.Expression = Expression;
        this.Type = Type;
    }


    public String getExpression() {
        return Expression;
    }

    public void setExpression(String Expression) {
        this.Expression = Expression;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }


}