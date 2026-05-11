





import java.util.List;
import java.util.ArrayList;

public class jpdl31_TaskType  {

    private String blocking;
    private String swimlane;
    private String name;
    private String signalling;
    private String description;
    private String group;
    private String duedate;
    private String priority;





    private List<jpdl31_EventType> jpdl31_eventtypes;




    private jpdl31_DocumentRoot jpdl31_documentroot;




    private List<jpdl31_AssignmentType> jpdl31_assignmenttypes;




    private List<jpdl31_Delegation> jpdl31_delegations;




    private jpdl31_ProcessDefinitionType jpdl31_processdefinitiontype;


    public jpdl31_TaskType(
        String blocking,        String swimlane,        String name,        String signalling,        String description,        String group,        String duedate,        String priority    ) {
        this.blocking = blocking;
        this.swimlane = swimlane;
        this.name = name;
        this.signalling = signalling;
        this.description = description;
        this.group = group;
        this.duedate = duedate;
        this.priority = priority;
        this.jpdl31_eventtypes = new ArrayList<>();
        this.jpdl31_assignmenttypes = new ArrayList<>();
        this.jpdl31_delegations = new ArrayList<>();
    }

    public jpdl31_TaskType(
        String blocking,        String swimlane,        String name,        String signalling,        String description,        String group,        String duedate,        String priority        ArrayList<jpdl31_EventType> jpdl31_eventtypes,        ArrayList<jpdl31_AssignmentType> jpdl31_assignmenttypes,        ArrayList<jpdl31_Delegation> jpdl31_delegations    ) {
        this.blocking = blocking;
        this.swimlane = swimlane;
        this.name = name;
        this.signalling = signalling;
        this.description = description;
        this.group = group;
        this.duedate = duedate;
        this.priority = priority;
        this.jpdl31_eventtypes = jpdl31_eventtypes;
        this.jpdl31_assignmenttypes = jpdl31_assignmenttypes;
        this.jpdl31_delegations = jpdl31_delegations;
    }

    public String getBlocking() {
        return blocking;
    }

    public void setBlocking(String blocking) {
        this.blocking = blocking;
    }
    public String getSwimlane() {
        return swimlane;
    }

    public void setSwimlane(String swimlane) {
        this.swimlane = swimlane;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSignalling() {
        return signalling;
    }

    public void setSignalling(String signalling) {
        this.signalling = signalling;
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
    public String getDuedate() {
        return duedate;
    }

    public void setDuedate(String duedate) {
        this.duedate = duedate;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }

    public List<jpdl31_EventType> getJpdl31_eventtypes() {
        return jpdl31_eventtypes;
    }

    public void addJpdl31_eventtype(Jpdl31_eventtype jpdl31_eventtype) {
        this.jpdl31_eventtypes.add(jpdl31_eventtype);
    }
    public jpdl31_DocumentRoot getJpdl31_documentroot() {
        return jpdl31_documentroot;
    }

    public void setJpdl31_documentroot(jpdl31_DocumentRoot jpdl31_documentroot) {
        this.jpdl31_documentroot = jpdl31_documentroot;
    }
    public List<jpdl31_AssignmentType> getJpdl31_assignmenttypes() {
        return jpdl31_assignmenttypes;
    }

    public void addJpdl31_assignmenttype(Jpdl31_assignmenttype jpdl31_assignmenttype) {
        this.jpdl31_assignmenttypes.add(jpdl31_assignmenttype);
    }
    public List<jpdl31_Delegation> getJpdl31_delegations() {
        return jpdl31_delegations;
    }

    public void addJpdl31_delegation(Jpdl31_delegation jpdl31_delegation) {
        this.jpdl31_delegations.add(jpdl31_delegation);
    }
    public jpdl31_ProcessDefinitionType getJpdl31_processdefinitiontype() {
        return jpdl31_processdefinitiontype;
    }

    public void setJpdl31_processdefinitiontype(jpdl31_ProcessDefinitionType jpdl31_processdefinitiontype) {
        this.jpdl31_processdefinitiontype = jpdl31_processdefinitiontype;
    }

}