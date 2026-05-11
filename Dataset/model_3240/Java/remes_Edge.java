





import java.util.List;
import java.util.ArrayList;

public class remes_Edge  {

    private String actionBody;
    private String actionGuard;





    private remes_ExitPoint remes_exitpoint;




    private LogicalRoot logicalroot;




    private remes_EntryPoint remes_entrypoint;




    private remes_ExitPoint remes_exitpoint;




    private remes_EntryPoint remes_entrypoint;


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

    public remes_ExitPoint getRemes_exitpoint() {
        return remes_exitpoint;
    }

    public void setRemes_exitpoint(remes_ExitPoint remes_exitpoint) {
        this.remes_exitpoint = remes_exitpoint;
    }
    public LogicalRoot getLogicalroot() {
        return logicalroot;
    }

    public void setLogicalroot(LogicalRoot logicalroot) {
        this.logicalroot = logicalroot;
    }
    public remes_EntryPoint getRemes_entrypoint() {
        return remes_entrypoint;
    }

    public void setRemes_entrypoint(remes_EntryPoint remes_entrypoint) {
        this.remes_entrypoint = remes_entrypoint;
    }
    public remes_ExitPoint getRemes_exitpoint() {
        return remes_exitpoint;
    }

    public void setRemes_exitpoint(remes_ExitPoint remes_exitpoint) {
        this.remes_exitpoint = remes_exitpoint;
    }
    public remes_EntryPoint getRemes_entrypoint() {
        return remes_entrypoint;
    }

    public void setRemes_entrypoint(remes_EntryPoint remes_entrypoint) {
        this.remes_entrypoint = remes_entrypoint;
    }

}