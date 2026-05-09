





import java.util.List;
import java.util.ArrayList;

public class ACG_LabelStat extends EmitStat {

    private String name;





    private Expression expression;


    public ACG_LabelStat(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}