





import java.util.List;
import java.util.ArrayList;

public class jpdl31_StartStateType  {

    private String name;
    private String group;





    private jpdl31_ProcessDefinitionType jpdl31_processdefinitiontype;




    private jpdl31_DocumentRoot jpdl31_documentroot;




    private List<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes;




    private List<jpdl31_TaskType> jpdl31_tasktypes;




    private List<jpdl31_EventType> jpdl31_eventtypes;


    public jpdl31_StartStateType(
        String name,        String group    ) {
        this.name = name;
        this.group = group;
        this.jpdl31_exceptionhandlertypes = new ArrayList<>();
        this.jpdl31_tasktypes = new ArrayList<>();
        this.jpdl31_eventtypes = new ArrayList<>();
    }

    public jpdl31_StartStateType(
        String name,        String group        ArrayList<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes,        ArrayList<jpdl31_TaskType> jpdl31_tasktypes,        ArrayList<jpdl31_EventType> jpdl31_eventtypes    ) {
        this.name = name;
        this.group = group;
        this.jpdl31_exceptionhandlertypes = jpdl31_exceptionhandlertypes;
        this.jpdl31_tasktypes = jpdl31_tasktypes;
        this.jpdl31_eventtypes = jpdl31_eventtypes;
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

    public jpdl31_ProcessDefinitionType getJpdl31_processdefinitiontype() {
        return jpdl31_processdefinitiontype;
    }

    public void setJpdl31_processdefinitiontype(jpdl31_ProcessDefinitionType jpdl31_processdefinitiontype) {
        this.jpdl31_processdefinitiontype = jpdl31_processdefinitiontype;
    }
    public jpdl31_DocumentRoot getJpdl31_documentroot() {
        return jpdl31_documentroot;
    }

    public void setJpdl31_documentroot(jpdl31_DocumentRoot jpdl31_documentroot) {
        this.jpdl31_documentroot = jpdl31_documentroot;
    }
    public List<jpdl31_ExceptionHandlerType> getJpdl31_exceptionhandlertypes() {
        return jpdl31_exceptionhandlertypes;
    }

    public void addJpdl31_exceptionhandlertype(Jpdl31_exceptionhandlertype jpdl31_exceptionhandlertype) {
        this.jpdl31_exceptionhandlertypes.add(jpdl31_exceptionhandlertype);
    }
    public List<jpdl31_TaskType> getJpdl31_tasktypes() {
        return jpdl31_tasktypes;
    }

    public void addJpdl31_tasktype(Jpdl31_tasktype jpdl31_tasktype) {
        this.jpdl31_tasktypes.add(jpdl31_tasktype);
    }
    public List<jpdl31_EventType> getJpdl31_eventtypes() {
        return jpdl31_eventtypes;
    }

    public void addJpdl31_eventtype(Jpdl31_eventtype jpdl31_eventtype) {
        this.jpdl31_eventtypes.add(jpdl31_eventtype);
    }

}