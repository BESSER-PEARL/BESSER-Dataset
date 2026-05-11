





import java.util.List;
import java.util.ArrayList;

public class avm_CalculatedValue extends ValueExpressionType {

    private String Type;
    private String Expression;



    public avm_CalculatedValue(
        String Type,        String Expression    ) {
        super(
        );
        this.Type = Type;
        this.Expression = Expression;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getExpression() {
        return Expression;
    }

    public void setExpression(String Expression) {
        this.Expression = Expression;
    }


}