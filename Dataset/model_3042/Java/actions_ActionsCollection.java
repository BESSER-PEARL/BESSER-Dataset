





import java.util.List;
import java.util.ArrayList;

public class actions_ActionsCollection  {

    private int version;
    private String ns;
    private int id;





    private List<actions_Action> actions_actions;


    public actions_ActionsCollection(
        int version,        String ns,        int id    ) {
        this.version = version;
        this.ns = ns;
        this.id = id;
        this.actions_actions = new ArrayList<>();
    }

    public actions_ActionsCollection(
        int version,        String ns,        int id        ArrayList<actions_Action> actions_actions    ) {
        this.version = version;
        this.ns = ns;
        this.id = id;
        this.actions_actions = actions_actions;
    }

    public int getVersion() {
        return version;
    }

    public void setVersion(int version) {
        this.version = version;
    }
    public String getNs() {
        return ns;
    }

    public void setNs(String ns) {
        this.ns = ns;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<actions_Action> getActions_actions() {
        return actions_actions;
    }

    public void addActions_action(Actions_action actions_action) {
        this.actions_actions.add(actions_action);
    }

}