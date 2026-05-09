





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMActions_UnaryOperator extends ActionExpressionElement {

    private String operatorname;





    private FSMActions_ActionExpressionElement fsmactions_actionexpressionelement;


    public HALL_FSMActions_UnaryOperator(
        String operatorname    ) {
        super(
        );
        this.operatorname = operatorname;
    }


    public String getOperatorname() {
        return operatorname;
    }

    public void setOperatorname(String operatorname) {
        this.operatorname = operatorname;
    }

    public FSMActions_ActionExpressionElement getFsmactions_actionexpressionelement() {
        return fsmactions_actionexpressionelement;
    }

    public void setFsmactions_actionexpressionelement(FSMActions_ActionExpressionElement fsmactions_actionexpressionelement) {
        this.fsmactions_actionexpressionelement = fsmactions_actionexpressionelement;
    }

}