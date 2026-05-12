





import java.util.List;
import java.util.ArrayList;

public class Rules  {

    private boolean currentRules;
    private String attribute;



    public Rules(
        boolean currentRules,        String attribute    ) {
        this.currentRules = currentRules;
        this.attribute = attribute;
    }


    public boolean getCurrentrules() {
        return currentRules;
    }

    public void setCurrentrules(boolean currentRules) {
        this.currentRules = currentRules;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}