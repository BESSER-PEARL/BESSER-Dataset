





import java.util.List;
import java.util.ArrayList;

public class ACG_ForEachStat extends CompoundStat {






    private VariableDecl variabledecl;




    private Expression expression;


    public ACG_ForEachStat(
    ) {
        super(
        );
    }



    public VariableDecl getVariabledecl() {
        return variabledecl;
    }

    public void setVariabledecl(VariableDecl variabledecl) {
        this.variabledecl = variabledecl;
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}