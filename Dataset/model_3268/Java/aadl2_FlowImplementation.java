





import java.util.List;
import java.util.ArrayList;

public class aadl2_FlowImplementation extends ModalPath, ClassifierFeature, Flow {

    private String kind;





    private List<aadl2_FlowSegment> aadl2_flowsegments;




    private aadl2_FlowEnd aadl2_flowend;




    private aadl2_FlowEnd aadl2_flowend;


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
    public aadl2_FlowEnd getAadl2_flowend() {
        return aadl2_flowend;
    }

    public void setAadl2_flowend(aadl2_FlowEnd aadl2_flowend) {
        this.aadl2_flowend = aadl2_flowend;
    }
    public aadl2_FlowEnd getAadl2_flowend() {
        return aadl2_flowend;
    }

    public void setAadl2_flowend(aadl2_FlowEnd aadl2_flowend) {
        this.aadl2_flowend = aadl2_flowend;
    }

}