





import java.util.List;
import java.util.ArrayList;

public class jpdl32_TaskType  {

    private String description;
    private String group;
    private String swimlane;
    private String description1;
    private String duedate;
    private String notify;
    private String signalling;
    private String priority;
    private String name;
    private String blocking;





    private List<jpdl32_EventType> jpdl32_eventtypes;




    private jpdl32_StartStateType jpdl32_startstatetype;




    private jpdl32_ProcessDefinitionType jpdl32_processdefinitiontype;




    private List<jpdl32_Delegation> jpdl32_delegations;




    private List<jpdl32_AssignmentType> jpdl32_assignmenttypes;




    private jpdl32_DocumentRoot jpdl32_documentroot;


    public jpdl32_TaskType(
        String description,        String group,        String swimlane,        String description1,        String duedate,        String notify,        String signalling,        String priority,        String name,        String blocking    ) {
        this.description = description;
        this.group = group;
        this.swimlane = swimlane;
        this.description1 = description1;
        this.duedate = duedate;
        this.notify = notify;
        this.signalling = signalling;
        this.priority = priority;
        this.name = name;
        this.blocking = blocking;
        this.jpdl32_eventtypes = new ArrayList<>();
        this.jpdl32_delegations = new ArrayList<>();
        this.jpdl32_assignmenttypes = new ArrayList<>();
    }

    public jpdl32_TaskType(
        String description,        String group,        String swimlane,        String description1,        String duedate,        String notify,        String signalling,        String priority,        String name,        String blocking        ArrayList<jpdl32_EventType> jpdl32_eventtypes,        ArrayList<jpdl32_Delegation> jpdl32_delegations,        ArrayList<jpdl32_AssignmentType> jpdl32_assignmenttypes    ) {
        this.description = description;
        this.group = group;
        this.swimlane = swimlane;
        this.description1 = description1;
        this.duedate = duedate;
        this.notify = notify;
        this.signalling = signalling;
        this.priority = priority;
        this.name = name;
        this.blocking = blocking;
        this.jpdl32_eventtypes = jpdl32_eventtypes;
        this.jpdl32_delegations = jpdl32_delegations;
        this.jpdl32_assignmenttypes = jpdl32_assignmenttypes;
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
    public String getDescription1() {
        return description1;
    }

    public void setDescription1(String description1) {
        this.description1 = description1;
    }
    public String getDuedate() {
        return duedate;
    }

    public void setDuedate(String duedate) {
        this.duedate = duedate;
    }
    public String getNotify() {
        return notify;
    }

    public void setNotify(String notify) {
        this.notify = notify;
    }
    public String getSignalling() {
        return signalling;
    }

    public void setSignalling(String signalling) {
        this.signalling = signalling;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBlocking() {
        return blocking;
    }

    public void setBlocking(String blocking) {
        this.blocking = blocking;
    }

    public List<jpdl32_EventType> getJpdl32_eventtypes() {
        return jpdl32_eventtypes;
    }

    public void addJpdl32_eventtype(Jpdl32_eventtype jpdl32_eventtype) {
        this.jpdl32_eventtypes.add(jpdl32_eventtype);
    }
    public jpdl32_StartStateType getJpdl32_startstatetype() {
        return jpdl32_startstatetype;
    }

    public void setJpdl32_startstatetype(jpdl32_StartStateType jpdl32_startstatetype) {
        this.jpdl32_startstatetype = jpdl32_startstatetype;
    }
    public jpdl32_ProcessDefinitionType getJpdl32_processdefinitiontype() {
        return jpdl32_processdefinitiontype;
    }

    public void setJpdl32_processdefinitiontype(jpdl32_ProcessDefinitionType jpdl32_processdefinitiontype) {
        this.jpdl32_processdefinitiontype = jpdl32_processdefinitiontype;
    }
    public List<jpdl32_Delegation> getJpdl32_delegations() {
        return jpdl32_delegations;
    }

    public void addJpdl32_delegation(Jpdl32_delegation jpdl32_delegation) {
        this.jpdl32_delegations.add(jpdl32_delegation);
    }
    public List<jpdl32_AssignmentType> getJpdl32_assignmenttypes() {
        return jpdl32_assignmenttypes;
    }

    public void addJpdl32_assignmenttype(Jpdl32_assignmenttype jpdl32_assignmenttype) {
        this.jpdl32_assignmenttypes.add(jpdl32_assignmenttype);
    }
    public jpdl32_DocumentRoot getJpdl32_documentroot() {
        return jpdl32_documentroot;
    }

    public void setJpdl32_documentroot(jpdl32_DocumentRoot jpdl32_documentroot) {
        this.jpdl32_documentroot = jpdl32_documentroot;
    }

}