





import java.util.List;
import java.util.ArrayList;

public class Grafcet_Transition extends Element {

    private String condition;



    public Grafcet_Transition(
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