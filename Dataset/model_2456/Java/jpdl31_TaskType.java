





import java.util.List;
import java.util.ArrayList;

public class jpdl31_TaskType  {

    private String priority;
    private String duedate;
    private String blocking;
    private String description;
    private String group;
    private String swimlane;
    private String signalling;
    private String name;





    private jpdl31_StartStateType jpdl31_startstatetype;




    private List<jpdl31_Delegation> jpdl31_delegations;




    private List<jpdl31_AssignmentType> jpdl31_assignmenttypes;




    private jpdl31_DocumentRoot jpdl31_documentroot;




    private List<jpdl31_EventType> jpdl31_eventtypes;




    private jpdl31_ProcessDefinitionType jpdl31_processdefinitiontype;


    public jpdl31_TaskType(
        String priority,        String duedate,        String blocking,        String description,        String group,        String swimlane,        String signalling,        String name    ) {
        this.priority = priority;
        this.duedate = duedate;
        this.blocking = blocking;
        this.description = description;
        this.group = group;
        this.swimlane = swimlane;
        this.signalling = signalling;
        this.name = name;
        this.jpdl31_delegations = new ArrayList<>();
        this.jpdl31_assignmenttypes = new ArrayList<>();
        this.jpdl31_eventtypes = new ArrayList<>();
    }

    public jpdl31_TaskType(
        String priority,        String duedate,        String blocking,        String description,        String group,        String swimlane,        String signalling,        String name        ArrayList<jpdl31_Delegation> jpdl31_delegations,        ArrayList<jpdl31_AssignmentType> jpdl31_assignmenttypes,        ArrayList<jpdl31_EventType> jpdl31_eventtypes    ) {
        this.priority = priority;
        this.duedate = duedate;
        this.blocking = blocking;
        this.description = description;
        this.group = group;
        this.swimlane = swimlane;
        this.signalling = signalling;
        this.name = name;
        this.jpdl31_delegations = jpdl31_delegations;
        this.jpdl31_assignmenttypes = jpdl31_assignmenttypes;
        this.jpdl31_eventtypes = jpdl31_eventtypes;
    }

    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getDuedate() {
        return duedate;
    }

    public void setDuedate(String duedate) {
        this.duedate = duedate;
    }
    public String getBlocking() {
        return blocking;
    }

    public void setBlocking(String blocking) {
        this.blocking = blocking;
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
    public String getSwimlane() {
        return swimlane;
    }

    public void setSwimlane(String swimlane) {
        this.swimlane = swimlane;
    }
    public String getSignalling() {
        return signalling;
    }

    public void setSignalling(String signalling) {
        this.signalling = signalling;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jpdl31_StartStateType getJpdl31_startstatetype() {
        return jpdl31_startstatetype;
    }

    public void setJpdl31_startstatetype(jpdl31_StartStateType jpdl31_startstatetype) {
        this.jpdl31_startstatetype = jpdl31_startstatetype;
    }
    public List<jpdl31_Delegation> getJpdl31_delegations() {
        return jpdl31_delegations;
    }

    public void addJpdl31_delegation(Jpdl31_delegation jpdl31_delegation) {
        this.jpdl31_delegations.add(jpdl31_delegation);
    }
    public List<jpdl31_AssignmentType> getJpdl31_assignmenttypes() {
        return jpdl31_assignmenttypes;
    }

    public void addJpdl31_assignmenttype(Jpdl31_assignmenttype jpdl31_assignmenttype) {
        this.jpdl31_assignmenttypes.add(jpdl31_assignmenttype);
    }
    public jpdl31_DocumentRoot getJpdl31_documentroot() {
        return jpdl31_documentroot;
    }

    public void setJpdl31_documentroot(jpdl31_DocumentRoot jpdl31_documentroot) {
        this.jpdl31_documentroot = jpdl31_documentroot;
    }
    public List<jpdl31_EventType> getJpdl31_eventtypes() {
        return jpdl31_eventtypes;
    }

    public void addJpdl31_eventtype(Jpdl31_eventtype jpdl31_eventtype) {
        this.jpdl31_eventtypes.add(jpdl31_eventtype);
    }
    public jpdl31_ProcessDefinitionType getJpdl31_processdefinitiontype() {
        return jpdl31_processdefinitiontype;
    }

    public void setJpdl31_processdefinitiontype(jpdl31_ProcessDefinitionType jpdl31_processdefinitiontype) {
        this.jpdl31_processdefinitiontype = jpdl31_processdefinitiontype;
    }

}