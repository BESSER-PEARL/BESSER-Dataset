





import java.util.List;
import java.util.ArrayList;

public class ACG_AnalyzeStat extends CompoundStat {

    private String mode;





    private Expression expression;


    public ACG_AnalyzeStat(
        String mode    ) {
        super(
        );
        this.mode = mode;
    }


    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}