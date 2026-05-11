





import java.util.List;
import java.util.ArrayList;

public class behavioral_design_AbstractStatusVariable extends NamedElement {

    private boolean isStateGuarded;
    private boolean isAgent;



    public behavioral_design_AbstractStatusVariable(
        boolean isStateGuarded,        boolean isAgent    ) {
        super(
        );
        this.isStateGuarded = isStateGuarded;
        this.isAgent = isAgent;
    }


    public boolean getIsstateguarded() {
        return isStateGuarded;
    }

    public void setIsstateguarded(boolean isStateGuarded) {
        this.isStateGuarded = isStateGuarded;
    }
    public boolean getIsagent() {
        return isAgent;
    }

    public void setIsagent(boolean isAgent) {
        this.isAgent = isAgent;
    }


}