





import java.util.List;
import java.util.ArrayList;

public class jpdl32_NodeType  {

    private String description;
    private String name;
    private String async_;
    private String nodeContentElements;





    private jpdl32_MailType jpdl32_mailtype;




    private jpdl32_DocumentRoot jpdl32_documentroot;




    private jpdl32_CancelTimerType jpdl32_canceltimertype;




    private jpdl32_ScriptType jpdl32_scripttype;




    private List<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes;




    private List<jpdl32_EventType> jpdl32_eventtypes;




    private jpdl32_CreateTimerType jpdl32_createtimertype;




    private List<jpdl32_TransitionType> jpdl32_transitiontypes;


    public jpdl32_NodeType(
        String description,        String name,        String async_,        String nodeContentElements    ) {
        this.description = description;
        this.name = name;
        this.async_ = async_;
        this.nodeContentElements = nodeContentElements;
        this.jpdl32_exceptionhandlertypes = new ArrayList<>();
        this.jpdl32_eventtypes = new ArrayList<>();
        this.jpdl32_transitiontypes = new ArrayList<>();
    }

    public jpdl32_NodeType(
        String description,        String name,        String async_,        String nodeContentElements        ArrayList<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes,        ArrayList<jpdl32_EventType> jpdl32_eventtypes,        ArrayList<jpdl32_TransitionType> jpdl32_transitiontypes    ) {
        this.description = description;
        this.name = name;
        this.async_ = async_;
        this.nodeContentElements = nodeContentElements;
        this.jpdl32_exceptionhandlertypes = jpdl32_exceptionhandlertypes;
        this.jpdl32_eventtypes = jpdl32_eventtypes;
        this.jpdl32_transitiontypes = jpdl32_transitiontypes;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAsync_() {
        return async_;
    }

    public void setAsync_(String async_) {
        this.async_ = async_;
    }
    public String getNodecontentelements() {
        return nodeContentElements;
    }

    public void setNodecontentelements(String nodeContentElements) {
        this.nodeContentElements = nodeContentElements;
    }

    public jpdl32_MailType getJpdl32_mailtype() {
        return jpdl32_mailtype;
    }

    public void setJpdl32_mailtype(jpdl32_MailType jpdl32_mailtype) {
        this.jpdl32_mailtype = jpdl32_mailtype;
    }
    public jpdl32_DocumentRoot getJpdl32_documentroot() {
        return jpdl32_documentroot;
    }

    public void setJpdl32_documentroot(jpdl32_DocumentRoot jpdl32_documentroot) {
        this.jpdl32_documentroot = jpdl32_documentroot;
    }
    public jpdl32_CancelTimerType getJpdl32_canceltimertype() {
        return jpdl32_canceltimertype;
    }

    public void setJpdl32_canceltimertype(jpdl32_CancelTimerType jpdl32_canceltimertype) {
        this.jpdl32_canceltimertype = jpdl32_canceltimertype;
    }
    public jpdl32_ScriptType getJpdl32_scripttype() {
        return jpdl32_scripttype;
    }

    public void setJpdl32_scripttype(jpdl32_ScriptType jpdl32_scripttype) {
        this.jpdl32_scripttype = jpdl32_scripttype;
    }
    public List<jpdl32_ExceptionHandlerType> getJpdl32_exceptionhandlertypes() {
        return jpdl32_exceptionhandlertypes;
    }

    public void addJpdl32_exceptionhandlertype(Jpdl32_exceptionhandlertype jpdl32_exceptionhandlertype) {
        this.jpdl32_exceptionhandlertypes.add(jpdl32_exceptionhandlertype);
    }
    public List<jpdl32_EventType> getJpdl32_eventtypes() {
        return jpdl32_eventtypes;
    }

    public void addJpdl32_eventtype(Jpdl32_eventtype jpdl32_eventtype) {
        this.jpdl32_eventtypes.add(jpdl32_eventtype);
    }
    public jpdl32_CreateTimerType getJpdl32_createtimertype() {
        return jpdl32_createtimertype;
    }

    public void setJpdl32_createtimertype(jpdl32_CreateTimerType jpdl32_createtimertype) {
        this.jpdl32_createtimertype = jpdl32_createtimertype;
    }
    public List<jpdl32_TransitionType> getJpdl32_transitiontypes() {
        return jpdl32_transitiontypes;
    }

    public void addJpdl32_transitiontype(Jpdl32_transitiontype jpdl32_transitiontype) {
        this.jpdl32_transitiontypes.add(jpdl32_transitiontype);
    }

}