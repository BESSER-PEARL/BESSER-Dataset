





import java.util.List;
import java.util.ArrayList;

public class ACG_LetStat extends CompoundStat {






    private Expression expression;




    private VariableDecl variabledecl;


    public ACG_LetStat(
    ) {
        super(
        );
    }



    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }
    public VariableDecl getVariabledecl() {
        return variabledecl;
    }

    public void setVariabledecl(VariableDecl variabledecl) {
        this.variabledecl = variabledecl;
    }

}