





import java.util.List;
import java.util.ArrayList;

public class jpdl32_ProcessStateType  {

    private String async_;
    private String group;
    private String binding;
    private String description;
    private String name;





    private List<jpdl32_EventType> jpdl32_eventtypes;




    private jpdl32_DocumentRoot jpdl32_documentroot;




    private List<jpdl32_TransitionType> jpdl32_transitiontypes;




    private List<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes;




    private jpdl32_ProcessDefinitionType jpdl32_processdefinitiontype;


    public jpdl32_ProcessStateType(
        String async_,        String group,        String binding,        String description,        String name    ) {
        this.async_ = async_;
        this.group = group;
        this.binding = binding;
        this.description = description;
        this.name = name;
        this.jpdl32_eventtypes = new ArrayList<>();
        this.jpdl32_transitiontypes = new ArrayList<>();
        this.jpdl32_exceptionhandlertypes = new ArrayList<>();
    }

    public jpdl32_ProcessStateType(
        String async_,        String group,        String binding,        String description,        String name        ArrayList<jpdl32_EventType> jpdl32_eventtypes,        ArrayList<jpdl32_TransitionType> jpdl32_transitiontypes,        ArrayList<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes    ) {
        this.async_ = async_;
        this.group = group;
        this.binding = binding;
        this.description = description;
        this.name = name;
        this.jpdl32_eventtypes = jpdl32_eventtypes;
        this.jpdl32_transitiontypes = jpdl32_transitiontypes;
        this.jpdl32_exceptionhandlertypes = jpdl32_exceptionhandlertypes;
    }

    public String getAsync_() {
        return async_;
    }

    public void setAsync_(String async_) {
        this.async_ = async_;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getBinding() {
        return binding;
    }

    public void setBinding(String binding) {
        this.binding = binding;
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

    public List<jpdl32_EventType> getJpdl32_eventtypes() {
        return jpdl32_eventtypes;
    }

    public void addJpdl32_eventtype(Jpdl32_eventtype jpdl32_eventtype) {
        this.jpdl32_eventtypes.add(jpdl32_eventtype);
    }
    public jpdl32_DocumentRoot getJpdl32_documentroot() {
        return jpdl32_documentroot;
    }

    public void setJpdl32_documentroot(jpdl32_DocumentRoot jpdl32_documentroot) {
        this.jpdl32_documentroot = jpdl32_documentroot;
    }
    public List<jpdl32_TransitionType> getJpdl32_transitiontypes() {
        return jpdl32_transitiontypes;
    }

    public void addJpdl32_transitiontype(Jpdl32_transitiontype jpdl32_transitiontype) {
        this.jpdl32_transitiontypes.add(jpdl32_transitiontype);
    }
    public List<jpdl32_ExceptionHandlerType> getJpdl32_exceptionhandlertypes() {
        return jpdl32_exceptionhandlertypes;
    }

    public void addJpdl32_exceptionhandlertype(Jpdl32_exceptionhandlertype jpdl32_exceptionhandlertype) {
        this.jpdl32_exceptionhandlertypes.add(jpdl32_exceptionhandlertype);
    }
    public jpdl32_ProcessDefinitionType getJpdl32_processdefinitiontype() {
        return jpdl32_processdefinitiontype;
    }

    public void setJpdl32_processdefinitiontype(jpdl32_ProcessDefinitionType jpdl32_processdefinitiontype) {
        this.jpdl32_processdefinitiontype = jpdl32_processdefinitiontype;
    }

}