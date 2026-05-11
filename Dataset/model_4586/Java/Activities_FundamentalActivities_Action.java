





import java.util.List;
import java.util.ArrayList;

public class Activities_FundamentalActivities_Action extends ActivityNode {

    private boolean isLocallyReentrant;



    public Activities_FundamentalActivities_Action(
        boolean isLocallyReentrant    ) {
        super(
        );
        this.isLocallyReentrant = isLocallyReentrant;
    }


    public boolean getIslocallyreentrant() {
        return isLocallyReentrant;
    }

    public void setIslocallyreentrant(boolean isLocallyReentrant) {
        this.isLocallyReentrant = isLocallyReentrant;
    }


}