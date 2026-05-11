





import java.util.List;
import java.util.ArrayList;

public class jpdl32_TaskType  {

    private String signalling;
    private String notify;
    private String duedate;
    private String group;
    private String blocking;
    private String name;
    private String description;
    private String description1;
    private String priority;
    private String swimlane;





    private List<jpdl32_EventType> jpdl32_eventtypes;




    private List<jpdl32_Delegation> jpdl32_delegations;




    private List<jpdl32_AssignmentType> jpdl32_assignmenttypes;




    private jpdl32_DocumentRoot jpdl32_documentroot;


    public jpdl32_TaskType(
        String signalling,        String notify,        String duedate,        String group,        String blocking,        String name,        String description,        String description1,        String priority,        String swimlane    ) {
        this.signalling = signalling;
        this.notify = notify;
        this.duedate = duedate;
        this.group = group;
        this.blocking = blocking;
        this.name = name;
        this.description = description;
        this.description1 = description1;
        this.priority = priority;
        this.swimlane = swimlane;
        this.jpdl32_eventtypes = new ArrayList<>();
        this.jpdl32_delegations = new ArrayList<>();
        this.jpdl32_assignmenttypes = new ArrayList<>();
    }

    public jpdl32_TaskType(
        String signalling,        String notify,        String duedate,        String group,        String blocking,        String name,        String description,        String description1,        String priority,        String swimlane        ArrayList<jpdl32_EventType> jpdl32_eventtypes,        ArrayList<jpdl32_Delegation> jpdl32_delegations,        ArrayList<jpdl32_AssignmentType> jpdl32_assignmenttypes    ) {
        this.signalling = signalling;
        this.notify = notify;
        this.duedate = duedate;
        this.group = group;
        this.blocking = blocking;
        this.name = name;
        this.description = description;
        this.description1 = description1;
        this.priority = priority;
        this.swimlane = swimlane;
        this.jpdl32_eventtypes = jpdl32_eventtypes;
        this.jpdl32_delegations = jpdl32_delegations;
        this.jpdl32_assignmenttypes = jpdl32_assignmenttypes;
    }

    public String getSignalling() {
        return signalling;
    }

    public void setSignalling(String signalling) {
        this.signalling = signalling;
    }
    public String getNotify() {
        return notify;
    }

    public void setNotify(String notify) {
        this.notify = notify;
    }
    public String getDuedate() {
        return duedate;
    }

    public void setDuedate(String duedate) {
        this.duedate = duedate;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getBlocking() {
        return blocking;
    }

    public void setBlocking(String blocking) {
        this.blocking = blocking;
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
    public String getDescription1() {
        return description1;
    }

    public void setDescription1(String description1) {
        this.description1 = description1;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getSwimlane() {
        return swimlane;
    }

    public void setSwimlane(String swimlane) {
        this.swimlane = swimlane;
    }

    public List<jpdl32_EventType> getJpdl32_eventtypes() {
        return jpdl32_eventtypes;
    }

    public void addJpdl32_eventtype(Jpdl32_eventtype jpdl32_eventtype) {
        this.jpdl32_eventtypes.add(jpdl32_eventtype);
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