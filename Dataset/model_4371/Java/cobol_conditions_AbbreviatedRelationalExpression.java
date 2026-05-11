





import java.util.List;
import java.util.ArrayList;

public class cobol_conditions_AbbreviatedRelationalExpression extends NegatedAbbreviatedConditionalExpressionChild {






    private Negate negate;




    private RelationalOperator relationaloperator;




    private Is is;


    public cobol_conditions_AbbreviatedRelationalExpression(
    ) {
        super(
        );
    }



    public Negate getNegate() {
        return negate;
    }

    public void setNegate(Negate negate) {
        this.negate = negate;
    }
    public RelationalOperator getRelationaloperator() {
        return relationaloperator;
    }

    public void setRelationaloperator(RelationalOperator relationaloperator) {
        this.relationaloperator = relationaloperator;
    }
    public Is getIs() {
        return is;
    }

    public void setIs(Is is) {
        this.is = is;
    }

}