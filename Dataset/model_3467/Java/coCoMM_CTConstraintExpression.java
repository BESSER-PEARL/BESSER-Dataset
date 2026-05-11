





import java.util.List;
import java.util.ArrayList;

public class coCoMM_CTConstraintExpression  {

    private String op;





    private List<coCoMM_CTConstraintExpression> cocomm_ctconstraintexpressions;


    public coCoMM_CTConstraintExpression(
        String op    ) {
        this.op = op;
        this.cocomm_ctconstraintexpressions = new ArrayList<>();
    }

    public coCoMM_CTConstraintExpression(
        String op        ArrayList<coCoMM_CTConstraintExpression> cocomm_ctconstraintexpressions    ) {
        this.op = op;
        this.cocomm_ctconstraintexpressions = cocomm_ctconstraintexpressions;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public List<coCoMM_CTConstraintExpression> getCocomm_ctconstraintexpressions() {
        return cocomm_ctconstraintexpressions;
    }

    public void addCocomm_ctconstraintexpression(Cocomm_ctconstraintexpression cocomm_ctconstraintexpression) {
        this.cocomm_ctconstraintexpressions.add(cocomm_ctconstraintexpression);
    }

}