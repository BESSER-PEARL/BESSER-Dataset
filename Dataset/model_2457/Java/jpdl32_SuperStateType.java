





import java.util.List;
import java.util.ArrayList;

public class jpdl32_SuperStateType  {

    private String async_;
    private String description;
    private String group;
    private String name;





    private List<jpdl32_StateType> jpdl32_statetypes;




    private List<jpdl32_MailNodeType> jpdl32_mailnodetypes;




    private jpdl32_ProcessDefinitionType jpdl32_processdefinitiontype;




    private List<jpdl32_SuperStateType> jpdl32_superstatetypes;




    private List<jpdl32_ProcessStateType> jpdl32_processstatetypes;




    private List<jpdl32_ForkType> jpdl32_forktypes;




    private List<jpdl32_DecisionType> jpdl32_decisiontypes;




    private List<jpdl32_EventType> jpdl32_eventtypes;




    private List<jpdl32_JoinType> jpdl32_jointypes;




    private List<jpdl32_TransitionType> jpdl32_transitiontypes;




    private List<jpdl32_EndStateType> jpdl32_endstatetypes;




    private jpdl32_DocumentRoot jpdl32_documentroot;




    private List<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes;




    private List<jpdl32_NodeType> jpdl32_nodetypes;


    public jpdl32_SuperStateType(
        String async_,        String description,        String group,        String name    ) {
        this.async_ = async_;
        this.description = description;
        this.group = group;
        this.name = name;
        this.jpdl32_statetypes = new ArrayList<>();
        this.jpdl32_mailnodetypes = new ArrayList<>();
        this.jpdl32_superstatetypes = new ArrayList<>();
        this.jpdl32_processstatetypes = new ArrayList<>();
        this.jpdl32_forktypes = new ArrayList<>();
        this.jpdl32_decisiontypes = new ArrayList<>();
        this.jpdl32_eventtypes = new ArrayList<>();
        this.jpdl32_jointypes = new ArrayList<>();
        this.jpdl32_transitiontypes = new ArrayList<>();
        this.jpdl32_endstatetypes = new ArrayList<>();
        this.jpdl32_exceptionhandlertypes = new ArrayList<>();
        this.jpdl32_nodetypes = new ArrayList<>();
    }

    public jpdl32_SuperStateType(
        String async_,        String description,        String group,        String name        ArrayList<jpdl32_StateType> jpdl32_statetypes,        ArrayList<jpdl32_MailNodeType> jpdl32_mailnodetypes,        ArrayList<jpdl32_SuperStateType> jpdl32_superstatetypes,        ArrayList<jpdl32_ProcessStateType> jpdl32_processstatetypes,        ArrayList<jpdl32_ForkType> jpdl32_forktypes,        ArrayList<jpdl32_DecisionType> jpdl32_decisiontypes,        ArrayList<jpdl32_EventType> jpdl32_eventtypes,        ArrayList<jpdl32_JoinType> jpdl32_jointypes,        ArrayList<jpdl32_TransitionType> jpdl32_transitiontypes,        ArrayList<jpdl32_EndStateType> jpdl32_endstatetypes,        ArrayList<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes,        ArrayList<jpdl32_NodeType> jpdl32_nodetypes    ) {
        this.async_ = async_;
        this.description = description;
        this.group = group;
        this.name = name;
        this.jpdl32_statetypes = jpdl32_statetypes;
        this.jpdl32_mailnodetypes = jpdl32_mailnodetypes;
        this.jpdl32_superstatetypes = jpdl32_superstatetypes;
        this.jpdl32_processstatetypes = jpdl32_processstatetypes;
        this.jpdl32_forktypes = jpdl32_forktypes;
        this.jpdl32_decisiontypes = jpdl32_decisiontypes;
        this.jpdl32_eventtypes = jpdl32_eventtypes;
        this.jpdl32_jointypes = jpdl32_jointypes;
        this.jpdl32_transitiontypes = jpdl32_transitiontypes;
        this.jpdl32_endstatetypes = jpdl32_endstatetypes;
        this.jpdl32_exceptionhandlertypes = jpdl32_exceptionhandlertypes;
        this.jpdl32_nodetypes = jpdl32_nodetypes;
    }

    public String getAsync_() {
        return async_;
    }

    public void setAsync_(String async_) {
        this.async_ = async_;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<jpdl32_StateType> getJpdl32_statetypes() {
        return jpdl32_statetypes;
    }

    public void addJpdl32_statetype(Jpdl32_statetype jpdl32_statetype) {
        this.jpdl32_statetypes.add(jpdl32_statetype);
    }
    public List<jpdl32_MailNodeType> getJpdl32_mailnodetypes() {
        return jpdl32_mailnodetypes;
    }

    public void addJpdl32_mailnodetype(Jpdl32_mailnodetype jpdl32_mailnodetype) {
        this.jpdl32_mailnodetypes.add(jpdl32_mailnodetype);
    }
    public jpdl32_ProcessDefinitionType getJpdl32_processdefinitiontype() {
        return jpdl32_processdefinitiontype;
    }

    public void setJpdl32_processdefinitiontype(jpdl32_ProcessDefinitionType jpdl32_processdefinitiontype) {
        this.jpdl32_processdefinitiontype = jpdl32_processdefinitiontype;
    }
    public List<jpdl32_SuperStateType> getJpdl32_superstatetypes() {
        return jpdl32_superstatetypes;
    }

    public void addJpdl32_superstatetype(Jpdl32_superstatetype jpdl32_superstatetype) {
        this.jpdl32_superstatetypes.add(jpdl32_superstatetype);
    }
    public List<jpdl32_ProcessStateType> getJpdl32_processstatetypes() {
        return jpdl32_processstatetypes;
    }

    public void addJpdl32_processstatetype(Jpdl32_processstatetype jpdl32_processstatetype) {
        this.jpdl32_processstatetypes.add(jpdl32_processstatetype);
    }
    public List<jpdl32_ForkType> getJpdl32_forktypes() {
        return jpdl32_forktypes;
    }

    public void addJpdl32_forktype(Jpdl32_forktype jpdl32_forktype) {
        this.jpdl32_forktypes.add(jpdl32_forktype);
    }
    public List<jpdl32_DecisionType> getJpdl32_decisiontypes() {
        return jpdl32_decisiontypes;
    }

    public void addJpdl32_decisiontype(Jpdl32_decisiontype jpdl32_decisiontype) {
        this.jpdl32_decisiontypes.add(jpdl32_decisiontype);
    }
    public List<jpdl32_EventType> getJpdl32_eventtypes() {
        return jpdl32_eventtypes;
    }

    public void addJpdl32_eventtype(Jpdl32_eventtype jpdl32_eventtype) {
        this.jpdl32_eventtypes.add(jpdl32_eventtype);
    }
    public List<jpdl32_JoinType> getJpdl32_jointypes() {
        return jpdl32_jointypes;
    }

    public void addJpdl32_jointype(Jpdl32_jointype jpdl32_jointype) {
        this.jpdl32_jointypes.add(jpdl32_jointype);
    }
    public List<jpdl32_TransitionType> getJpdl32_transitiontypes() {
        return jpdl32_transitiontypes;
    }

    public void addJpdl32_transitiontype(Jpdl32_transitiontype jpdl32_transitiontype) {
        this.jpdl32_transitiontypes.add(jpdl32_transitiontype);
    }
    public List<jpdl32_EndStateType> getJpdl32_endstatetypes() {
        return jpdl32_endstatetypes;
    }

    public void addJpdl32_endstatetype(Jpdl32_endstatetype jpdl32_endstatetype) {
        this.jpdl32_endstatetypes.add(jpdl32_endstatetype);
    }
    public jpdl32_DocumentRoot getJpdl32_documentroot() {
        return jpdl32_documentroot;
    }

    public void setJpdl32_documentroot(jpdl32_DocumentRoot jpdl32_documentroot) {
        this.jpdl32_documentroot = jpdl32_documentroot;
    }
    public List<jpdl32_ExceptionHandlerType> getJpdl32_exceptionhandlertypes() {
        return jpdl32_exceptionhandlertypes;
    }

    public void addJpdl32_exceptionhandlertype(Jpdl32_exceptionhandlertype jpdl32_exceptionhandlertype) {
        this.jpdl32_exceptionhandlertypes.add(jpdl32_exceptionhandlertype);
    }
    public List<jpdl32_NodeType> getJpdl32_nodetypes() {
        return jpdl32_nodetypes;
    }

    public void addJpdl32_nodetype(Jpdl32_nodetype jpdl32_nodetype) {
        this.jpdl32_nodetypes.add(jpdl32_nodetype);
    }

}