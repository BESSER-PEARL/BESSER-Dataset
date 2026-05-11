





import java.util.List;
import java.util.ArrayList;

public class jpdl32_JoinType  {

    private String nodeContentElements;
    private String async_;
    private String description;
    private String name;





    private List<jpdl32_EventType> jpdl32_eventtypes;




    private List<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes;




    private List<jpdl32_TransitionType> jpdl32_transitiontypes;




    private jpdl32_DocumentRoot jpdl32_documentroot;


    public jpdl32_JoinType(
        String nodeContentElements,        String async_,        String description,        String name    ) {
        this.nodeContentElements = nodeContentElements;
        this.async_ = async_;
        this.description = description;
        this.name = name;
        this.jpdl32_eventtypes = new ArrayList<>();
        this.jpdl32_exceptionhandlertypes = new ArrayList<>();
        this.jpdl32_transitiontypes = new ArrayList<>();
    }

    public jpdl32_JoinType(
        String nodeContentElements,        String async_,        String description,        String name        ArrayList<jpdl32_EventType> jpdl32_eventtypes,        ArrayList<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes,        ArrayList<jpdl32_TransitionType> jpdl32_transitiontypes    ) {
        this.nodeContentElements = nodeContentElements;
        this.async_ = async_;
        this.description = description;
        this.name = name;
        this.jpdl32_eventtypes = jpdl32_eventtypes;
        this.jpdl32_exceptionhandlertypes = jpdl32_exceptionhandlertypes;
        this.jpdl32_transitiontypes = jpdl32_transitiontypes;
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

}