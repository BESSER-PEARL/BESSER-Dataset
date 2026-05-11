





import java.util.List;
import java.util.ArrayList;

public class jpdl31_NodeType  {

    private String description;
    private String nodeContentElements;
    private String async_;
    private String name;





    private jpdl31_ActionType jpdl31_actiontype;




    private List<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes;




    private jpdl31_DocumentRoot jpdl31_documentroot;




    private jpdl31_ScriptType jpdl31_scripttype;




    private List<jpdl31_EventType> jpdl31_eventtypes;




    private jpdl31_CreateTimerType jpdl31_createtimertype;




    private jpdl31_CancelTimerType jpdl31_canceltimertype;


    public jpdl31_NodeType(
        String description,        String nodeContentElements,        String async_,        String name    ) {
        this.description = description;
        this.nodeContentElements = nodeContentElements;
        this.async_ = async_;
        this.name = name;
        this.jpdl31_exceptionhandlertypes = new ArrayList<>();
        this.jpdl31_eventtypes = new ArrayList<>();
    }

    public jpdl31_NodeType(
        String description,        String nodeContentElements,        String async_,        String name        ArrayList<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes,        ArrayList<jpdl31_EventType> jpdl31_eventtypes    ) {
        this.description = description;
        this.nodeContentElements = nodeContentElements;
        this.async_ = async_;
        this.name = name;
        this.jpdl31_exceptionhandlertypes = jpdl31_exceptionhandlertypes;
        this.jpdl31_eventtypes = jpdl31_eventtypes;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getNodecontentelements() {
        return nodeContentElements;
    }

    public void setNodecontentelements(String nodeContentElements) {
        this.nodeContentElements = nodeContentElements;
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

    public jpdl31_ActionType getJpdl31_actiontype() {
        return jpdl31_actiontype;
    }

    public void setJpdl31_actiontype(jpdl31_ActionType jpdl31_actiontype) {
        this.jpdl31_actiontype = jpdl31_actiontype;
    }
    public List<jpdl31_ExceptionHandlerType> getJpdl31_exceptionhandlertypes() {
        return jpdl31_exceptionhandlertypes;
    }

    public void addJpdl31_exceptionhandlertype(Jpdl31_exceptionhandlertype jpdl31_exceptionhandlertype) {
        this.jpdl31_exceptionhandlertypes.add(jpdl31_exceptionhandlertype);
    }
    public jpdl31_DocumentRoot getJpdl31_documentroot() {
        return jpdl31_documentroot;
    }

    public void setJpdl31_documentroot(jpdl31_DocumentRoot jpdl31_documentroot) {
        this.jpdl31_documentroot = jpdl31_documentroot;
    }
    public jpdl31_ScriptType getJpdl31_scripttype() {
        return jpdl31_scripttype;
    }

    public void setJpdl31_scripttype(jpdl31_ScriptType jpdl31_scripttype) {
        this.jpdl31_scripttype = jpdl31_scripttype;
    }
    public List<jpdl31_EventType> getJpdl31_eventtypes() {
        return jpdl31_eventtypes;
    }

    public void addJpdl31_eventtype(Jpdl31_eventtype jpdl31_eventtype) {
        this.jpdl31_eventtypes.add(jpdl31_eventtype);
    }
    public jpdl31_CreateTimerType getJpdl31_createtimertype() {
        return jpdl31_createtimertype;
    }

    public void setJpdl31_createtimertype(jpdl31_CreateTimerType jpdl31_createtimertype) {
        this.jpdl31_createtimertype = jpdl31_createtimertype;
    }
    public jpdl31_CancelTimerType getJpdl31_canceltimertype() {
        return jpdl31_canceltimertype;
    }

    public void setJpdl31_canceltimertype(jpdl31_CancelTimerType jpdl31_canceltimertype) {
        this.jpdl31_canceltimertype = jpdl31_canceltimertype;
    }

}