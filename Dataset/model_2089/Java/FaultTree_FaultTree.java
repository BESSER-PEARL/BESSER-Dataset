





import java.util.List;
import java.util.ArrayList;

public class FaultTree_FaultTree  {

    private String message;
    private String name;
    private String faultTreeType;





    private FaultTree_EObject faulttree_eobject;




    private FaultTree_Event faulttree_event;




    private List<FaultTree_Event> faulttree_events;


    public FaultTree_FaultTree(
        String message,        String name,        String faultTreeType    ) {
        this.message = message;
        this.name = name;
        this.faultTreeType = faultTreeType;
        this.faulttree_events = new ArrayList<>();
    }

    public FaultTree_FaultTree(
        String message,        String name,        String faultTreeType        ArrayList<FaultTree_Event> faulttree_events    ) {
        this.message = message;
        this.name = name;
        this.faultTreeType = faultTreeType;
        this.faulttree_events = faulttree_events;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFaulttreetype() {
        return faultTreeType;
    }

    public void setFaulttreetype(String faultTreeType) {
        this.faultTreeType = faultTreeType;
    }

    public FaultTree_EObject getFaulttree_eobject() {
        return faulttree_eobject;
    }

    public void setFaulttree_eobject(FaultTree_EObject faulttree_eobject) {
        this.faulttree_eobject = faulttree_eobject;
    }
    public FaultTree_Event getFaulttree_event() {
        return faulttree_event;
    }

    public void setFaulttree_event(FaultTree_Event faulttree_event) {
        this.faulttree_event = faulttree_event;
    }
    public List<FaultTree_Event> getFaulttree_events() {
        return faulttree_events;
    }

    public void addFaulttree_event(Faulttree_event faulttree_event) {
        this.faulttree_events.add(faulttree_event);
    }

}