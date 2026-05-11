





import java.util.List;
import java.util.ArrayList;

public class RDM_Turnout extends TrackElement {

    private String currentDirection;
    private String switchingDirection;



    public RDM_Turnout(
        String currentDirection,        String switchingDirection    ) {
        super(
        );
        this.currentDirection = currentDirection;
        this.switchingDirection = switchingDirection;
    }


    public String getCurrentdirection() {
        return currentDirection;
    }

    public void setCurrentdirection(String currentDirection) {
        this.currentDirection = currentDirection;
    }
    public String getSwitchingdirection() {
        return switchingDirection;
    }

    public void setSwitchingdirection(String switchingDirection) {
        this.switchingDirection = switchingDirection;
    }


}