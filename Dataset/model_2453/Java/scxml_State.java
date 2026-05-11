





import java.util.List;
import java.util.ArrayList;

public class scxml_State extends NamedElement {

    private String id;





    private List<scxml_FinalState> scxml_finalstates;




    private scxml_ServiceTemplate scxml_servicetemplate;




    private scxml_State scxml_state;




    private List<scxml_HistoryState> scxml_historystates;




    private List<scxml_Anchor> scxml_anchors;




    private List<scxml_Parallel> scxml_parallels;




    private scxml_Parallel scxml_parallel;




    private List<scxml_Invoke> scxml_invokes;


    public scxml_State(
        String id    ) {
        super(
        );
        this.id = id;
        this.scxml_finalstates = new ArrayList<>();
        this.scxml_historystates = new ArrayList<>();
        this.scxml_anchors = new ArrayList<>();
        this.scxml_parallels = new ArrayList<>();
        this.scxml_invokes = new ArrayList<>();
    }

    public scxml_State(
        String id        ArrayList<scxml_FinalState> scxml_finalstates,        ArrayList<scxml_HistoryState> scxml_historystates,        ArrayList<scxml_Anchor> scxml_anchors,        ArrayList<scxml_Parallel> scxml_parallels,        ArrayList<scxml_Invoke> scxml_invokes    ) {
        this.id = id;
        this.scxml_finalstates = scxml_finalstates;
        this.scxml_historystates = scxml_historystates;
        this.scxml_anchors = scxml_anchors;
        this.scxml_parallels = scxml_parallels;
        this.scxml_invokes = scxml_invokes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<scxml_FinalState> getScxml_finalstates() {
        return scxml_finalstates;
    }

    public void addScxml_finalstate(Scxml_finalstate scxml_finalstate) {
        this.scxml_finalstates.add(scxml_finalstate);
    }
    public scxml_ServiceTemplate getScxml_servicetemplate() {
        return scxml_servicetemplate;
    }

    public void setScxml_servicetemplate(scxml_ServiceTemplate scxml_servicetemplate) {
        this.scxml_servicetemplate = scxml_servicetemplate;
    }
    public scxml_State getScxml_state() {
        return scxml_state;
    }

    public void setScxml_state(scxml_State scxml_state) {
        this.scxml_state = scxml_state;
    }
    public List<scxml_HistoryState> getScxml_historystates() {
        return scxml_historystates;
    }

    public void addScxml_historystate(Scxml_historystate scxml_historystate) {
        this.scxml_historystates.add(scxml_historystate);
    }
    public List<scxml_Anchor> getScxml_anchors() {
        return scxml_anchors;
    }

    public void addScxml_anchor(Scxml_anchor scxml_anchor) {
        this.scxml_anchors.add(scxml_anchor);
    }
    public List<scxml_Parallel> getScxml_parallels() {
        return scxml_parallels;
    }

    public void addScxml_parallel(Scxml_parallel scxml_parallel) {
        this.scxml_parallels.add(scxml_parallel);
    }
    public scxml_Parallel getScxml_parallel() {
        return scxml_parallel;
    }

    public void setScxml_parallel(scxml_Parallel scxml_parallel) {
        this.scxml_parallel = scxml_parallel;
    }
    public List<scxml_Invoke> getScxml_invokes() {
        return scxml_invokes;
    }

    public void addScxml_invoke(Scxml_invoke scxml_invoke) {
        this.scxml_invokes.add(scxml_invoke);
    }

}