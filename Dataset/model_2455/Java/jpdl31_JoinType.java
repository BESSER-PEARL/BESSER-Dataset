





import java.util.List;
import java.util.ArrayList;

public class jpdl31_JoinType  {

    private String async_;
    private String nodeContentElements;
    private String name;





    private List<jpdl31_EventType> jpdl31_eventtypes;




    private List<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes;




    private jpdl31_DocumentRoot jpdl31_documentroot;


    public jpdl31_JoinType(
        String async_,        String nodeContentElements,        String name    ) {
        this.async_ = async_;
        this.nodeContentElements = nodeContentElements;
        this.name = name;
        this.jpdl31_eventtypes = new ArrayList<>();
        this.jpdl31_exceptionhandlertypes = new ArrayList<>();
    }

    public jpdl31_JoinType(
        String async_,        String nodeContentElements,        String name        ArrayList<jpdl31_EventType> jpdl31_eventtypes,        ArrayList<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes    ) {
        this.async_ = async_;
        this.nodeContentElements = nodeContentElements;
        this.name = name;
        this.jpdl31_eventtypes = jpdl31_eventtypes;
        this.jpdl31_exceptionhandlertypes = jpdl31_exceptionhandlertypes;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

}