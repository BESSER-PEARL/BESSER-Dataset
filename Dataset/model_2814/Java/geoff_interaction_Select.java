





import java.util.List;
import java.util.ArrayList;

public class geoff_interaction_Select extends Interaction {

    private boolean multi;
    private String condition;



    public geoff_interaction_Select(
        boolean multi,        String condition    ) {
        super(
        );
        this.multi = multi;
        this.condition = condition;
    }


    public boolean getMulti() {
        return multi;
    }

    public void setMulti(boolean multi) {
        this.multi = multi;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }


}