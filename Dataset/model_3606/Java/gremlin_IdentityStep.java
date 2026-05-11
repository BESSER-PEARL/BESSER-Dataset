





import java.util.List;
import java.util.ArrayList;

public class gremlin_IdentityStep extends Step {

    private boolean needed;



    public gremlin_IdentityStep(
        boolean needed    ) {
        super(
        );
        this.needed = needed;
    }


    public boolean getNeeded() {
        return needed;
    }

    public void setNeeded(boolean needed) {
        this.needed = needed;
    }


}