





import java.util.List;
import java.util.ArrayList;

public class remes_Edge  {

    private String actionGuard;
    private String actionBody;



    public remes_Edge(
        String actionGuard,        String actionBody    ) {
        this.actionGuard = actionGuard;
        this.actionBody = actionBody;
    }


    public String getActionguard() {
        return actionGuard;
    }

    public void setActionguard(String actionGuard) {
        this.actionGuard = actionGuard;
    }
    public String getActionbody() {
        return actionBody;
    }

    public void setActionbody(String actionBody) {
        this.actionBody = actionBody;
    }


}