





import java.util.List;
import java.util.ArrayList;

public class jpdl31_StateType  {

    private String name;
    private String async_;
    private String nodeContentElements;





    private List<jpdl31_EventType> jpdl31_eventtypes;




    private List<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes;




    private jpdl31_DocumentRoot jpdl31_documentroot;




    private jpdl31_ProcessDefinitionType jpdl31_processdefinitiontype;




    private List<jpdl31_TimerType> jpdl31_timertypes;


    public jpdl31_StateType(
        String name,        String async_,        String nodeContentElements    ) {
        this.name = name;
        this.async_ = async_;
        this.nodeContentElements = nodeContentElements;
        this.jpdl31_eventtypes = new ArrayList<>();
        this.jpdl31_exceptionhandlertypes = new ArrayList<>();
        this.jpdl31_timertypes = new ArrayList<>();
    }

    public jpdl31_StateType(
        String name,        String async_,        String nodeContentElements        ArrayList<jpdl31_EventType> jpdl31_eventtypes,        ArrayList<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes,        ArrayList<jpdl31_TimerType> jpdl31_timertypes    ) {
        this.name = name;
        this.async_ = async_;
        this.nodeContentElements = nodeContentElements;
        this.jpdl31_eventtypes = jpdl31_eventtypes;
        this.jpdl31_exceptionhandlertypes = jpdl31_exceptionhandlertypes;
        this.jpdl31_timertypes = jpdl31_timertypes;
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

    public List<jpdl31_EventType> getJpdl31_eventtypes() {
        return jpdl31_eventtypes;
    }

    public void addJpdl31_eventtype(Jpdl31_eventtype jpdl31_eventtype) {
        this.jpdl31_eventtypes.add(jpdl31_eventtype);
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
    public jpdl31_ProcessDefinitionType getJpdl31_processdefinitiontype() {
        return jpdl31_processdefinitiontype;
    }

    public void setJpdl31_processdefinitiontype(jpdl31_ProcessDefinitionType jpdl31_processdefinitiontype) {
        this.jpdl31_processdefinitiontype = jpdl31_processdefinitiontype;
    }
    public List<jpdl31_TimerType> getJpdl31_timertypes() {
        return jpdl31_timertypes;
    }

    public void addJpdl31_timertype(Jpdl31_timertype jpdl31_timertype) {
        this.jpdl31_timertypes.add(jpdl31_timertype);
    }

}