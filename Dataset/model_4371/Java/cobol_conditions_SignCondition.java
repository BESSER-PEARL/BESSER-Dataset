





import java.util.List;
import java.util.ArrayList;

public class cobol_conditions_SignCondition extends NegatedConditionalExpressionChild {






    private SignOperator signoperator;




    private Negate negate;




    private SimpleConditionChild simpleconditionchild;




    private Is is;


    public cobol_conditions_SignCondition(
    ) {
        super(
        );
    }



    public SignOperator getSignoperator() {
        return signoperator;
    }

    public void setSignoperator(SignOperator signoperator) {
        this.signoperator = signoperator;
    }
    public Negate getNegate() {
        return negate;
    }

    public void setNegate(Negate negate) {
        this.negate = negate;
    }
    public SimpleConditionChild getSimpleconditionchild() {
        return simpleconditionchild;
    }

    public void setSimpleconditionchild(SimpleConditionChild simpleconditionchild) {
        this.simpleconditionchild = simpleconditionchild;
    }
    public Is getIs() {
        return is;
    }

    public void setIs(Is is) {
        this.is = is;
    }

}