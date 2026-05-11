





import java.util.List;
import java.util.ArrayList;

public class gast_variables_FormalParameter extends Variable {

    private boolean passedByReference;



    public gast_variables_FormalParameter(
        boolean passedByReference    ) {
        super(
        );
        this.passedByReference = passedByReference;
    }


    public boolean getPassedbyreference() {
        return passedByReference;
    }

    public void setPassedbyreference(boolean passedByReference) {
        this.passedByReference = passedByReference;
    }


}