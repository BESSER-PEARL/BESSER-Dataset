





import java.util.List;
import java.util.ArrayList;

public class aadl2_EndToEndFlow extends EndToEndFlowElement, ModalPath, FlowFeature {






    private List<aadl2_EndToEndFlowSegment> aadl2_endtoendflowsegments;




    private aadl2_EndToEndFlow aadl2_endtoendflow;


    public aadl2_EndToEndFlow(
    ) {
        super(
        );
        this.aadl2_endtoendflowsegments = new ArrayList<>();
    }

    public aadl2_EndToEndFlow(
        ArrayList<aadl2_EndToEndFlowSegment> aadl2_endtoendflowsegments    ) {
        this.aadl2_endtoendflowsegments = aadl2_endtoendflowsegments;
    }


    public List<aadl2_EndToEndFlowSegment> getAadl2_endtoendflowsegments() {
        return aadl2_endtoendflowsegments;
    }

    public void addAadl2_endtoendflowsegment(Aadl2_endtoendflowsegment aadl2_endtoendflowsegment) {
        this.aadl2_endtoendflowsegments.add(aadl2_endtoendflowsegment);
    }
    public aadl2_EndToEndFlow getAadl2_endtoendflow() {
        return aadl2_endtoendflow;
    }

    public void setAadl2_endtoendflow(aadl2_EndToEndFlow aadl2_endtoendflow) {
        this.aadl2_endtoendflow = aadl2_endtoendflow;
    }

}