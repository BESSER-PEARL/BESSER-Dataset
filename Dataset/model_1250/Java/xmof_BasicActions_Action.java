





import java.util.List;
import java.util.ArrayList;

public class xmof_BasicActions_Action extends ExecutableNode {

    private boolean locallyReentrant;



    public xmof_BasicActions_Action(
        boolean locallyReentrant    ) {
        super(
        );
        this.locallyReentrant = locallyReentrant;
    }


    public boolean getLocallyreentrant() {
        return locallyReentrant;
    }

    public void setLocallyreentrant(boolean locallyReentrant) {
        this.locallyReentrant = locallyReentrant;
    }


}