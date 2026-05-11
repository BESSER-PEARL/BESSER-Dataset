





import java.util.List;
import java.util.ArrayList;

public class avm_ComplexFormula extends Formula {

    private String Expression;



    public avm_ComplexFormula(
        String Expression    ) {
        super(
        );
        this.Expression = Expression;
    }


    public String getExpression() {
        return Expression;
    }

    public void setExpression(String Expression) {
        this.Expression = Expression;
    }


}