





import java.util.List;
import java.util.ArrayList;

public class useCases_Condition extends StepAlternative {

    private String condition;



    public useCases_Condition(
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