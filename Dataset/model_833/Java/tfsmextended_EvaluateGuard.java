





import java.util.List;
import java.util.ArrayList;

public class tfsmextended_EvaluateGuard extends Guard {

    private String condition;



    public tfsmextended_EvaluateGuard(
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