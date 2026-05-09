





import java.util.List;
import java.util.ArrayList;

public class model_state_Transition extends UnicaseModelElement {

    private String condition;



    public model_state_Transition(
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