





import java.util.List;
import java.util.ArrayList;

public class tfsm_plaink3_EvaluateGuard extends Guard {

    private String condition;



    public tfsm_plaink3_EvaluateGuard(
        String condition    ) {
        super(
        );
        this.condition = condition;
    }


    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }


}