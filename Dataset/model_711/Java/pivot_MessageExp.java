





import java.util.List;
import java.util.ArrayList;

public class pivot_MessageExp extends OCLExpression {






    private pivot_CallOperationAction pivot_calloperationaction;




    private pivot_SendSignalAction pivot_sendsignalaction;


    public pivot_MessageExp(
    ) {
        super(
        );
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

}