





import java.util.List;
import java.util.ArrayList;

public class robochart_OperationSig extends NamedElement {

    private boolean terminates;



    public robochart_OperationSig(
        boolean terminates    ) {
        super(
        );
        this.terminates = terminates;
    }


    public boolean getTerminates() {
        return terminates;
    }

    public void setTerminates(boolean terminates) {
        this.terminates = terminates;
    }


}