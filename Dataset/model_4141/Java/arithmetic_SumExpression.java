





import java.util.List;
import java.util.ArrayList;

public class arithmetic_SumExpression extends Expression {

    private int lower;
    private int upper;





    private arithmetic_DeclaredParameter arithmetic_declaredparameter;




    private arithmetic_Expression arithmetic_expression;


    public arithmetic_SumExpression(
        int lower,        int upper    ) {
        super(
        );
        this.lower = lower;
        this.upper = upper;
    }


    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }

    public arithmetic_DeclaredParameter getArithmetic_declaredparameter() {
        return arithmetic_declaredparameter;
    }

    public void setArithmetic_declaredparameter(arithmetic_DeclaredParameter arithmetic_declaredparameter) {
        this.arithmetic_declaredparameter = arithmetic_declaredparameter;
    }
    public arithmetic_Expression getArithmetic_expression() {
        return arithmetic_expression;
    }

    public void setArithmetic_expression(arithmetic_Expression arithmetic_expression) {
        this.arithmetic_expression = arithmetic_expression;
    }

}