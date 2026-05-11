





import java.util.List;
import java.util.ArrayList;

public class sql_Event extends ModelElement {

    private String condition;
    private String action;



    public sql_Event(
        String condition,        String action    ) {
        super(
        );
        this.condition = condition;
        this.action = action;
    }


    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }


}