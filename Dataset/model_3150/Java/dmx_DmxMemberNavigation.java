





import java.util.List;
import java.util.ArrayList;

public class dmx_DmxMemberNavigation extends DExpression {

    private boolean explicitOperationCall;
    private boolean before;





    private dmx_DExpression dmx_dexpression;


    public dmx_DmxMemberNavigation(
        boolean explicitOperationCall,        boolean before    ) {
        super(
        );
        this.explicitOperationCall = explicitOperationCall;
        this.before = before;
    }


    public boolean getExplicitoperationcall() {
        return explicitOperationCall;
    }

    public void setExplicitoperationcall(boolean explicitOperationCall) {
        this.explicitOperationCall = explicitOperationCall;
    }
    public boolean getBefore() {
        return before;
    }

    public void setBefore(boolean before) {
        this.before = before;
    }

    public dmx_DExpression getDmx_dexpression() {
        return dmx_dexpression;
    }

    public void setDmx_dexpression(dmx_DExpression dmx_dexpression) {
        this.dmx_dexpression = dmx_dexpression;
    }

}