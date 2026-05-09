





import java.util.List;
import java.util.ArrayList;

public class henshin_GraphElement  {

    private String action;
    private String presenceCondition;



    public henshin_GraphElement(
        String action,        String presenceCondition    ) {
        this.action = action;
        this.presenceCondition = presenceCondition;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getPresencecondition() {
        return presenceCondition;
    }

    public void setPresencecondition(String presenceCondition) {
        this.presenceCondition = presenceCondition;
    }


}