





import java.util.List;
import java.util.ArrayList;

public class jpdl32_StartStateType  {

    private String group;
    private String name;
    private String description;





    private List<jpdl32_TaskType> jpdl32_tasktypes;




    private List<jpdl32_EventType> jpdl32_eventtypes;




    private List<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes;




    private List<jpdl32_TransitionType> jpdl32_transitiontypes;




    private jpdl32_DocumentRoot jpdl32_documentroot;




    private jpdl32_ProcessDefinitionType jpdl32_processdefinitiontype;


    public jpdl32_StartStateType(
        String group,        String name,        String description    ) {
        this.group = group;
        this.name = name;
        this.description = description;
        this.jpdl32_tasktypes = new ArrayList<>();
        this.jpdl32_eventtypes = new ArrayList<>();
        this.jpdl32_exceptionhandlertypes = new ArrayList<>();
        this.jpdl32_transitiontypes = new ArrayList<>();
    }

    public jpdl32_StartStateType(
        String group,        String name,        String description        ArrayList<jpdl32_TaskType> jpdl32_tasktypes,        ArrayList<jpdl32_EventType> jpdl32_eventtypes,        ArrayList<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes,        ArrayList<jpdl32_TransitionType> jpdl32_transitiontypes    ) {
        this.group = group;
        this.name = name;
        this.description = description;
        this.jpdl32_tasktypes = jpdl32_tasktypes;
        this.jpdl32_eventtypes = jpdl32_eventtypes;
        this.jpdl32_exceptionhandlertypes = jpdl32_exceptionhandlertypes;
        this.jpdl32_transitiontypes = jpdl32_transitiontypes;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<jpdl32_TaskType> getJpdl32_tasktypes() {
        return jpdl32_tasktypes;
    }

    public void addJpdl32_tasktype(Jpdl32_tasktype jpdl32_tasktype) {
        this.jpdl32_tasktypes.add(jpdl32_tasktype);
    }
    public List<jpdl32_EventType> getJpdl32_eventtypes() {
        return jpdl32_eventtypes;
    }

    public void addJpdl32_eventtype(Jpdl32_eventtype jpdl32_eventtype) {
        this.jpdl32_eventtypes.add(jpdl32_eventtype);
    }
    public List<jpdl32_ExceptionHandlerType> getJpdl32_exceptionhandlertypes() {
        return jpdl32_exceptionhandlertypes;
    }

    public void addJpdl32_exceptionhandlertype(Jpdl32_exceptionhandlertype jpdl32_exceptionhandlertype) {
        this.jpdl32_exceptionhandlertypes.add(jpdl32_exceptionhandlertype);
    }
    public List<jpdl32_TransitionType> getJpdl32_transitiontypes() {
        return jpdl32_transitiontypes;
    }

    public void addJpdl32_transitiontype(Jpdl32_transitiontype jpdl32_transitiontype) {
        this.jpdl32_transitiontypes.add(jpdl32_transitiontype);
    }
    public jpdl32_DocumentRoot getJpdl32_documentroot() {
        return jpdl32_documentroot;
    }

    public void setJpdl32_documentroot(jpdl32_DocumentRoot jpdl32_documentroot) {
        this.jpdl32_documentroot = jpdl32_documentroot;
    }
    public jpdl32_ProcessDefinitionType getJpdl32_processdefinitiontype() {
        return jpdl32_processdefinitiontype;
    }

    public void setJpdl32_processdefinitiontype(jpdl32_ProcessDefinitionType jpdl32_processdefinitiontype) {
        this.jpdl32_processdefinitiontype = jpdl32_processdefinitiontype;
    }

}