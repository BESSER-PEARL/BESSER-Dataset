





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_expressions_IncDecExpression extends Expression {

    private boolean beforeExpression;
    private boolean increment;



    public timedAutomata_expressions_IncDecExpression(
        boolean beforeExpression,        boolean increment    ) {
        super(
        );
        this.beforeExpression = beforeExpression;
        this.increment = increment;
    }


    public boolean getBeforeexpression() {
        return beforeExpression;
    }

    public void setBeforeexpression(boolean beforeExpression) {
        this.beforeExpression = beforeExpression;
    }
    public boolean getIncrement() {
        return increment;
    }

    public void setIncrement(boolean increment) {
        this.increment = increment;
    }


}