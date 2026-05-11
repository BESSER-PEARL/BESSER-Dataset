





import java.util.List;
import java.util.ArrayList;

public class PolicyEngine_TimeExpression extends Expression {

    private int TimeBound;





    private PolicyEngine_Timer policyengine_timer;


    public PolicyEngine_TimeExpression(
        int TimeBound    ) {
        super(
        );
        this.TimeBound = TimeBound;
    }


    public int getTimebound() {
        return TimeBound;
    }

    public void setTimebound(int TimeBound) {
        this.TimeBound = TimeBound;
    }

    public PolicyEngine_Timer getPolicyengine_timer() {
        return policyengine_timer;
    }

    public void setPolicyengine_timer(PolicyEngine_Timer policyengine_timer) {
        this.policyengine_timer = policyengine_timer;
    }

}