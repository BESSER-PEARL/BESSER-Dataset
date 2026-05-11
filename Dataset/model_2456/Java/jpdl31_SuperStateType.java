





import java.util.List;
import java.util.ArrayList;

public class jpdl31_SuperStateType  {

    private String async_;
    private String name;
    private String group;





    private List<jpdl31_ForkType> jpdl31_forktypes;




    private List<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes;




    private List<jpdl31_NodeType> jpdl31_nodetypes;




    private List<jpdl31_ProcessStateType> jpdl31_processstatetypes;




    private List<jpdl31_StateType> jpdl31_statetypes;




    private jpdl31_SuperStateType jpdl31_superstatetype;




    private List<jpdl31_EventType> jpdl31_eventtypes;




    private jpdl31_DocumentRoot jpdl31_documentroot;




    private jpdl31_ProcessDefinitionType jpdl31_processdefinitiontype;




    private List<jpdl31_EndStateType> jpdl31_endstatetypes;




    private List<jpdl31_DecisionType> jpdl31_decisiontypes;


    public jpdl31_SuperStateType(
        String async_,        String name,        String group    ) {
        this.async_ = async_;
        this.name = name;
        this.group = group;
        this.jpdl31_forktypes = new ArrayList<>();
        this.jpdl31_exceptionhandlertypes = new ArrayList<>();
        this.jpdl31_nodetypes = new ArrayList<>();
        this.jpdl31_processstatetypes = new ArrayList<>();
        this.jpdl31_statetypes = new ArrayList<>();
        this.jpdl31_eventtypes = new ArrayList<>();
        this.jpdl31_endstatetypes = new ArrayList<>();
        this.jpdl31_decisiontypes = new ArrayList<>();
    }

    public jpdl31_SuperStateType(
        String async_,        String name,        String group        ArrayList<jpdl31_ForkType> jpdl31_forktypes,        ArrayList<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes,        ArrayList<jpdl31_NodeType> jpdl31_nodetypes,        ArrayList<jpdl31_ProcessStateType> jpdl31_processstatetypes,        ArrayList<jpdl31_StateType> jpdl31_statetypes,        ArrayList<jpdl31_EventType> jpdl31_eventtypes,        ArrayList<jpdl31_EndStateType> jpdl31_endstatetypes,        ArrayList<jpdl31_DecisionType> jpdl31_decisiontypes    ) {
        this.async_ = async_;
        this.name = name;
        this.group = group;
        this.jpdl31_forktypes = jpdl31_forktypes;
        this.jpdl31_exceptionhandlertypes = jpdl31_exceptionhandlertypes;
        this.jpdl31_nodetypes = jpdl31_nodetypes;
        this.jpdl31_processstatetypes = jpdl31_processstatetypes;
        this.jpdl31_statetypes = jpdl31_statetypes;
        this.jpdl31_eventtypes = jpdl31_eventtypes;
        this.jpdl31_endstatetypes = jpdl31_endstatetypes;
        this.jpdl31_decisiontypes = jpdl31_decisiontypes;
    }

    public String getAsync_() {
        return async_;
    }

    public void setAsync_(String async_) {
        this.async_ = async_;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<jpdl31_ForkType> getJpdl31_forktypes() {
        return jpdl31_forktypes;
    }

    public void addJpdl31_forktype(Jpdl31_forktype jpdl31_forktype) {
        this.jpdl31_forktypes.add(jpdl31_forktype);
    }
    public List<jpdl31_ExceptionHandlerType> getJpdl31_exceptionhandlertypes() {
        return jpdl31_exceptionhandlertypes;
    }

    public void addJpdl31_exceptionhandlertype(Jpdl31_exceptionhandlertype jpdl31_exceptionhandlertype) {
        this.jpdl31_exceptionhandlertypes.add(jpdl31_exceptionhandlertype);
    }
    public List<jpdl31_NodeType> getJpdl31_nodetypes() {
        return jpdl31_nodetypes;
    }

    public void addJpdl31_nodetype(Jpdl31_nodetype jpdl31_nodetype) {
        this.jpdl31_nodetypes.add(jpdl31_nodetype);
    }
    public List<jpdl31_ProcessStateType> getJpdl31_processstatetypes() {
        return jpdl31_processstatetypes;
    }

    public void addJpdl31_processstatetype(Jpdl31_processstatetype jpdl31_processstatetype) {
        this.jpdl31_processstatetypes.add(jpdl31_processstatetype);
    }
    public List<jpdl31_StateType> getJpdl31_statetypes() {
        return jpdl31_statetypes;
    }

    public void addJpdl31_statetype(Jpdl31_statetype jpdl31_statetype) {
        this.jpdl31_statetypes.add(jpdl31_statetype);
    }
    public jpdl31_SuperStateType getJpdl31_superstatetype() {
        return jpdl31_superstatetype;
    }

    public void setJpdl31_superstatetype(jpdl31_SuperStateType jpdl31_superstatetype) {
        this.jpdl31_superstatetype = jpdl31_superstatetype;
    }
    public List<jpdl31_EventType> getJpdl31_eventtypes() {
        return jpdl31_eventtypes;
    }

    public void addJpdl31_eventtype(Jpdl31_eventtype jpdl31_eventtype) {
        this.jpdl31_eventtypes.add(jpdl31_eventtype);
    }
    public jpdl31_DocumentRoot getJpdl31_documentroot() {
        return jpdl31_documentroot;
    }

    public void setJpdl31_documentroot(jpdl31_DocumentRoot jpdl31_documentroot) {
        this.jpdl31_documentroot = jpdl31_documentroot;
    }
    public jpdl31_ProcessDefinitionType getJpdl31_processdefinitiontype() {
        return jpdl31_processdefinitiontype;
    }

    public void setJpdl31_processdefinitiontype(jpdl31_ProcessDefinitionType jpdl31_processdefinitiontype) {
        this.jpdl31_processdefinitiontype = jpdl31_processdefinitiontype;
    }
    public List<jpdl31_EndStateType> getJpdl31_endstatetypes() {
        return jpdl31_endstatetypes;
    }

    public void addJpdl31_endstatetype(Jpdl31_endstatetype jpdl31_endstatetype) {
        this.jpdl31_endstatetypes.add(jpdl31_endstatetype);
    }
    public List<jpdl31_DecisionType> getJpdl31_decisiontypes() {
        return jpdl31_decisiontypes;
    }

    public void addJpdl31_decisiontype(Jpdl31_decisiontype jpdl31_decisiontype) {
        this.jpdl31_decisiontypes.add(jpdl31_decisiontype);
    }

}