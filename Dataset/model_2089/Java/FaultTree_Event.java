





import java.util.List;
import java.util.ArrayList;

public class FaultTree_Event  {

    private String name;
    private String subEventLogic;
    private int referenceCount;
    private String assignedProbability;
    private String scale;
    private String message;
    private String type;
    private String computedProbability;
    private int k;





    private List<FaultTree_Event> faulttree_events;


    public FaultTree_Event(
        String name,        String subEventLogic,        int referenceCount,        String assignedProbability,        String scale,        String message,        String type,        String computedProbability,        int k    ) {
        this.name = name;
        this.subEventLogic = subEventLogic;
        this.referenceCount = referenceCount;
        this.assignedProbability = assignedProbability;
        this.scale = scale;
        this.message = message;
        this.type = type;
        this.computedProbability = computedProbability;
        this.k = k;
        this.faulttree_events = new ArrayList<>();
    }

    public FaultTree_Event(
        String name,        String subEventLogic,        int referenceCount,        String assignedProbability,        String scale,        String message,        String type,        String computedProbability,        int k        ArrayList<FaultTree_Event> faulttree_events    ) {
        this.name = name;
        this.subEventLogic = subEventLogic;
        this.referenceCount = referenceCount;
        this.assignedProbability = assignedProbability;
        this.scale = scale;
        this.message = message;
        this.type = type;
        this.computedProbability = computedProbability;
        this.k = k;
        this.faulttree_events = faulttree_events;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSubeventlogic() {
        return subEventLogic;
    }

    public void setSubeventlogic(String subEventLogic) {
        this.subEventLogic = subEventLogic;
    }
    public int getReferencecount() {
        return referenceCount;
    }

    public void setReferencecount(int referenceCount) {
        this.referenceCount = referenceCount;
    }
    public String getAssignedprobability() {
        return assignedProbability;
    }

    public void setAssignedprobability(String assignedProbability) {
        this.assignedProbability = assignedProbability;
    }
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getComputedprobability() {
        return computedProbability;
    }

    public void setComputedprobability(String computedProbability) {
        this.computedProbability = computedProbability;
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

}