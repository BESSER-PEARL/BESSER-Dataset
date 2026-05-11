





import java.util.List;
import java.util.ArrayList;

public class FaultTree_Event  {

    private String message;
    private int referenceCount;
    private float assignedProbability;
    private float computedProbability;
    private String name;
    private boolean sharedEvent;
    private String subEventLogic;
    private String type;
    private int k;





    private List<FaultTree_Event> faulttree_events;




    private FaultTree_FaultTree faulttree_faulttree;




    private FaultTree_FaultTree faulttree_faulttree;


    public FaultTree_Event(
        String message,        int referenceCount,        float assignedProbability,        float computedProbability,        String name,        boolean sharedEvent,        String subEventLogic,        String type,        int k    ) {
        this.message = message;
        this.referenceCount = referenceCount;
        this.assignedProbability = assignedProbability;
        this.computedProbability = computedProbability;
        this.name = name;
        this.sharedEvent = sharedEvent;
        this.subEventLogic = subEventLogic;
        this.type = type;
        this.k = k;
        this.faulttree_events = new ArrayList<>();
    }

    public FaultTree_Event(
        String message,        int referenceCount,        float assignedProbability,        float computedProbability,        String name,        boolean sharedEvent,        String subEventLogic,        String type,        int k        ArrayList<FaultTree_Event> faulttree_events    ) {
        this.message = message;
        this.referenceCount = referenceCount;
        this.assignedProbability = assignedProbability;
        this.computedProbability = computedProbability;
        this.name = name;
        this.sharedEvent = sharedEvent;
        this.subEventLogic = subEventLogic;
        this.type = type;
        this.k = k;
        this.faulttree_events = faulttree_events;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public int getReferencecount() {
        return referenceCount;
    }

    public void setReferencecount(int referenceCount) {
        this.referenceCount = referenceCount;
    }
    public float getAssignedprobability() {
        return assignedProbability;
    }

    public void setAssignedprobability(float assignedProbability) {
        this.assignedProbability = assignedProbability;
    }
    public float getComputedprobability() {
        return computedProbability;
    }

    public void setComputedprobability(float computedProbability) {
        this.computedProbability = computedProbability;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getSharedevent() {
        return sharedEvent;
    }

    public void setSharedevent(boolean sharedEvent) {
        this.sharedEvent = sharedEvent;
    }
    public String getSubeventlogic() {
        return subEventLogic;
    }

    public void setSubeventlogic(String subEventLogic) {
        this.subEventLogic = subEventLogic;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getK() {
        return k;
    }

    public void setK(int k) {
        this.k = k;
    }

    public List<FaultTree_Event> getFaulttree_events() {
        return faulttree_events;
    }

    public void addFaulttree_event(Faulttree_event faulttree_event) {
        this.faulttree_events.add(faulttree_event);
    }
    public FaultTree_FaultTree getFaulttree_faulttree() {
        return faulttree_faulttree;
    }

    public void setFaulttree_faulttree(FaultTree_FaultTree faulttree_faulttree) {
        this.faulttree_faulttree = faulttree_faulttree;
    }
    public FaultTree_FaultTree getFaulttree_faulttree() {
        return faulttree_faulttree;
    }

    public void setFaulttree_faulttree(FaultTree_FaultTree faulttree_faulttree) {
        this.faulttree_faulttree = faulttree_faulttree;
    }

}