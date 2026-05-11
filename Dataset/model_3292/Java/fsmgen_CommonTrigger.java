





import java.util.List;
import java.util.ArrayList;

public class fsmgen_CommonTrigger extends FSMGenElement {

    private boolean hasGuard;
    private String trigger;





    private fsmgen_Node fsmgen_node;




    private List<fsmgen_Link> fsmgen_links;


    public fsmgen_CommonTrigger(
        boolean hasGuard,        String trigger    ) {
        super(
        );
        this.hasGuard = hasGuard;
        this.trigger = trigger;
        this.fsmgen_links = new ArrayList<>();
    }

    public fsmgen_CommonTrigger(
        boolean hasGuard,        String trigger        ArrayList<fsmgen_Link> fsmgen_links    ) {
        this.hasGuard = hasGuard;
        this.trigger = trigger;
        this.fsmgen_links = fsmgen_links;
    }

    public boolean getHasguard() {
        return hasGuard;
    }

    public void setHasguard(boolean hasGuard) {
        this.hasGuard = hasGuard;
    }
    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }

    public fsmgen_Node getFsmgen_node() {
        return fsmgen_node;
    }

    public void setFsmgen_node(fsmgen_Node fsmgen_node) {
        this.fsmgen_node = fsmgen_node;
    }
    public List<fsmgen_Link> getFsmgen_links() {
        return fsmgen_links;
    }

    public void addFsmgen_link(Fsmgen_link fsmgen_link) {
        this.fsmgen_links.add(fsmgen_link);
    }

}