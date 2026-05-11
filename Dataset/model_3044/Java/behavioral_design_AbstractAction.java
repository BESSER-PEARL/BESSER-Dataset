





import java.util.List;
import java.util.ArrayList;

public class behavioral_design_AbstractAction extends NamedElement {

    private boolean isPreconditionFixed;
    private boolean isAgent;



    public behavioral_design_AbstractAction(
        boolean isPreconditionFixed,        boolean isAgent    ) {
        super(
        );
        this.isPreconditionFixed = isPreconditionFixed;
        this.isAgent = isAgent;
    }


    public boolean getIspreconditionfixed() {
        return isPreconditionFixed;
    }

    public void setIspreconditionfixed(boolean isPreconditionFixed) {
        this.isPreconditionFixed = isPreconditionFixed;
    }
    public boolean getIsagent() {
        return isAgent;
    }

    public void setIsagent(boolean isAgent) {
        this.isAgent = isAgent;
    }


}