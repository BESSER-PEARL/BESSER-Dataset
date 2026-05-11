





import java.util.List;
import java.util.ArrayList;

public class remes_Edge  {

    private String actionBody;
    private String actionGuard;



    public remes_Edge(
        String actionBody,        String actionGuard    ) {
        this.actionBody = actionBody;
        this.actionGuard = actionGuard;
    }


    public String getActionbody() {
        return actionBody;
    }

    public void setActionbody(String actionBody) {
        this.actionBody = actionBody;
    }
    public String getActionguard() {
        return actionGuard;
    }

    public void setActionguard(String actionGuard) {
        this.actionGuard = actionGuard;
    }


}