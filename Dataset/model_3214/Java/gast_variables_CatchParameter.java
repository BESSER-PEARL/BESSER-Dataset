





import java.util.List;
import java.util.ArrayList;

public class gast_variables_CatchParameter extends Variable {

    private boolean rethrown;



    public gast_variables_CatchParameter(
        boolean rethrown    ) {
        super(
        );
        this.rethrown = rethrown;
    }


    public boolean getRethrown() {
        return rethrown;
    }

    public void setRethrown(boolean rethrown) {
        this.rethrown = rethrown;
    }


}