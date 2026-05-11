





import java.util.List;
import java.util.ArrayList;

public class aadl2_FlowImplementation extends ClassifierFeature, Flow, ModalPath {

    private String kind;





    private List<aadl2_FlowSegment> aadl2_flowsegments;


    public aadl2_FlowImplementation(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.aadl2_flowsegments = new ArrayList<>();
    }

    public aadl2_FlowImplementation(
        String kind        ArrayList<aadl2_FlowSegment> aadl2_flowsegments    ) {
        this.kind = kind;
        this.aadl2_flowsegments = aadl2_flowsegments;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public List<aadl2_FlowSegment> getAadl2_flowsegments() {
        return aadl2_flowsegments;
    }

    public void addAadl2_flowsegment(Aadl2_flowsegment aadl2_flowsegment) {
        this.aadl2_flowsegments.add(aadl2_flowsegment);
    }

}