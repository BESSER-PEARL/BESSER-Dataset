





import java.util.List;
import java.util.ArrayList;

public class RDM_TurnoutDesiredDirection extends RDMElement {

    private String desiredDirection;





    private RDM_Turnout rdm_turnout;


    public RDM_TurnoutDesiredDirection(
        String desiredDirection    ) {
        super(
        );
        this.desiredDirection = desiredDirection;
    }


    public String getDesireddirection() {
        return desiredDirection;
    }

    public void setDesireddirection(String desiredDirection) {
        this.desiredDirection = desiredDirection;
    }

    public RDM_Turnout getRdm_turnout() {
        return rdm_turnout;
    }

    public void setRdm_turnout(RDM_Turnout rdm_turnout) {
        this.rdm_turnout = rdm_turnout;
    }

}