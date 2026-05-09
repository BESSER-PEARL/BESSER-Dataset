





import java.util.List;
import java.util.ArrayList;

public class jbatch_Job  {

    private String id;
    private String version;
    private String restartable;
    private String group;





    private jbatch_Properties jbatch_properties;




    private List<jbatch_Flow> jbatch_flows;




    private jbatch_DocumentRoot jbatch_documentroot;




    private List<jbatch_Decision> jbatch_decisions;




    private jbatch_Listeners jbatch_listeners;




    private List<jbatch_Split> jbatch_splits;




    private List<jbatch_Step> jbatch_steps;


    public jbatch_Job(
        String id,        String version,        String restartable,        String group    ) {
        this.id = id;
        this.version = version;
        this.restartable = restartable;
        this.group = group;
        this.jbatch_flows = new ArrayList<>();
        this.jbatch_decisions = new ArrayList<>();
        this.jbatch_splits = new ArrayList<>();
        this.jbatch_steps = new ArrayList<>();
    }

    public jbatch_Job(
        String id,        String version,        String restartable,        String group        ArrayList<jbatch_Flow> jbatch_flows,        ArrayList<jbatch_Decision> jbatch_decisions,        ArrayList<jbatch_Split> jbatch_splits,        ArrayList<jbatch_Step> jbatch_steps    ) {
        this.id = id;
        this.version = version;
        this.restartable = restartable;
        this.group = group;
        this.jbatch_flows = jbatch_flows;
        this.jbatch_decisions = jbatch_decisions;
        this.jbatch_splits = jbatch_splits;
        this.jbatch_steps = jbatch_steps;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getRestartable() {
        return restartable;
    }

    public void setRestartable(String restartable) {
        this.restartable = restartable;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public jbatch_Properties getJbatch_properties() {
        return jbatch_properties;
    }

    public void setJbatch_properties(jbatch_Properties jbatch_properties) {
        this.jbatch_properties = jbatch_properties;
    }
    public List<jbatch_Flow> getJbatch_flows() {
        return jbatch_flows;
    }

    public void addJbatch_flow(Jbatch_flow jbatch_flow) {
        this.jbatch_flows.add(jbatch_flow);
    }
    public jbatch_DocumentRoot getJbatch_documentroot() {
        return jbatch_documentroot;
    }

    public void setJbatch_documentroot(jbatch_DocumentRoot jbatch_documentroot) {
        this.jbatch_documentroot = jbatch_documentroot;
    }
    public List<jbatch_Decision> getJbatch_decisions() {
        return jbatch_decisions;
    }

    public void addJbatch_decision(Jbatch_decision jbatch_decision) {
        this.jbatch_decisions.add(jbatch_decision);
    }
    public jbatch_Listeners getJbatch_listeners() {
        return jbatch_listeners;
    }

    public void setJbatch_listeners(jbatch_Listeners jbatch_listeners) {
        this.jbatch_listeners = jbatch_listeners;
    }
    public List<jbatch_Split> getJbatch_splits() {
        return jbatch_splits;
    }

    public void addJbatch_split(Jbatch_split jbatch_split) {
        this.jbatch_splits.add(jbatch_split);
    }
    public List<jbatch_Step> getJbatch_steps() {
        return jbatch_steps;
    }

    public void addJbatch_step(Jbatch_step jbatch_step) {
        this.jbatch_steps.add(jbatch_step);
    }

}