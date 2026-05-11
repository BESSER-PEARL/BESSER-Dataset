





import java.util.List;
import java.util.ArrayList;

public class workflow_ConditionalOutputPort extends OutputPort {

    private String condition;



    public workflow_ConditionalOutputPort(
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