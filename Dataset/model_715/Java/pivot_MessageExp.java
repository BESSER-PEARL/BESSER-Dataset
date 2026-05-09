





import java.util.List;
import java.util.ArrayList;

public class pivot_MessageExp extends OCLExpression {






    private pivot_OCLExpression pivot_oclexpression;




    private pivot_CallOperationAction pivot_calloperationaction;




    private pivot_SendSignalAction pivot_sendsignalaction;




    private List<pivot_OCLExpression> pivot_oclexpressions;


    public pivot_MessageExp(
    ) {
        super(
        );
        this.pivot_oclexpressions = new ArrayList<>();
    }

    public pivot_MessageExp(
        ArrayList<pivot_OCLExpression> pivot_oclexpressions    ) {
        this.pivot_oclexpressions = pivot_oclexpressions;
    }


    public pivot_OCLExpression getPivot_oclexpression() {
        return pivot_oclexpression;
    }

    public void setPivot_oclexpression(pivot_OCLExpression pivot_oclexpression) {
        this.pivot_oclexpression = pivot_oclexpression;
    }
    public pivot_CallOperationAction getPivot_calloperationaction() {
        return pivot_calloperationaction;
    }

    public void setPivot_calloperationaction(pivot_CallOperationAction pivot_calloperationaction) {
        this.pivot_calloperationaction = pivot_calloperationaction;
    }
    public pivot_SendSignalAction getPivot_sendsignalaction() {
        return pivot_sendsignalaction;
    }

    public void setPivot_sendsignalaction(pivot_SendSignalAction pivot_sendsignalaction) {
        this.pivot_sendsignalaction = pivot_sendsignalaction;
    }
    public List<pivot_OCLExpression> getPivot_oclexpressions() {
        return pivot_oclexpressions;
    }

    public void addPivot_oclexpression(Pivot_oclexpression pivot_oclexpression) {
        this.pivot_oclexpressions.add(pivot_oclexpression);
    }

}