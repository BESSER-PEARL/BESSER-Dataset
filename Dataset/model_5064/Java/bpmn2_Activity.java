





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Activity extends FlowNode {

    private int startQuantity;
    private int completionQuantity;
    private boolean isForCompensation;





    private List<bpmn2_BoundaryEvent> bpmn2_boundaryevents;




    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_BoundaryEvent bpmn2_boundaryevent;


    public bpmn2_Activity(
        int startQuantity,        int completionQuantity,        boolean isForCompensation    ) {
        super(
        );
        this.startQuantity = startQuantity;
        this.completionQuantity = completionQuantity;
        this.isForCompensation = isForCompensation;
        this.bpmn2_boundaryevents = new ArrayList<>();
    }

    public bpmn2_Activity(
        int startQuantity,        int completionQuantity,        boolean isForCompensation        ArrayList<bpmn2_BoundaryEvent> bpmn2_boundaryevents    ) {
        this.startQuantity = startQuantity;
        this.completionQuantity = completionQuantity;
        this.isForCompensation = isForCompensation;
        this.bpmn2_boundaryevents = bpmn2_boundaryevents;
    }

    public int getStartquantity() {
        return startQuantity;
    }

    public void setStartquantity(int startQuantity) {
        this.startQuantity = startQuantity;
    }
    public int getCompletionquantity() {
        return completionQuantity;
    }

    public void setCompletionquantity(int completionQuantity) {
        this.completionQuantity = completionQuantity;
    }
    public boolean getIsforcompensation() {
        return isForCompensation;
    }

    public void setIsforcompensation(boolean isForCompensation) {
        this.isForCompensation = isForCompensation;
    }

    public List<bpmn2_BoundaryEvent> getBpmn2_boundaryevents() {
        return bpmn2_boundaryevents;
    }

    public void addBpmn2_boundaryevent(Bpmn2_boundaryevent bpmn2_boundaryevent) {
        this.bpmn2_boundaryevents.add(bpmn2_boundaryevent);
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_BoundaryEvent getBpmn2_boundaryevent() {
        return bpmn2_boundaryevent;
    }

    public void setBpmn2_boundaryevent(bpmn2_BoundaryEvent bpmn2_boundaryevent) {
        this.bpmn2_boundaryevent = bpmn2_boundaryevent;
    }

}