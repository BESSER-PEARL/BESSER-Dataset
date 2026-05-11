





import java.util.List;
import java.util.ArrayList;

public class aadl2_Context extends NamedElement {






    private aadl2_EndToEndFlowSegment aadl2_endtoendflowsegment;




    private aadl2_FlowEnd aadl2_flowend;




    private aadl2_FlowSegment aadl2_flowsegment;




    private aadl2_ModeTransitionTrigger aadl2_modetransitiontrigger;




    private aadl2_ConnectedElement aadl2_connectedelement;


    public aadl2_Context(
    ) {
        super(
        );
    }



    public aadl2_EndToEndFlowSegment getAadl2_endtoendflowsegment() {
        return aadl2_endtoendflowsegment;
    }

    public void setAadl2_endtoendflowsegment(aadl2_EndToEndFlowSegment aadl2_endtoendflowsegment) {
        this.aadl2_endtoendflowsegment = aadl2_endtoendflowsegment;
    }
    public aadl2_FlowEnd getAadl2_flowend() {
        return aadl2_flowend;
    }

    public void setAadl2_flowend(aadl2_FlowEnd aadl2_flowend) {
        this.aadl2_flowend = aadl2_flowend;
    }
    public aadl2_FlowSegment getAadl2_flowsegment() {
        return aadl2_flowsegment;
    }

    public void setAadl2_flowsegment(aadl2_FlowSegment aadl2_flowsegment) {
        this.aadl2_flowsegment = aadl2_flowsegment;
    }
    public aadl2_ModeTransitionTrigger getAadl2_modetransitiontrigger() {
        return aadl2_modetransitiontrigger;
    }

    public void setAadl2_modetransitiontrigger(aadl2_ModeTransitionTrigger aadl2_modetransitiontrigger) {
        this.aadl2_modetransitiontrigger = aadl2_modetransitiontrigger;
    }
    public aadl2_ConnectedElement getAadl2_connectedelement() {
        return aadl2_connectedelement;
    }

    public void setAadl2_connectedelement(aadl2_ConnectedElement aadl2_connectedelement) {
        this.aadl2_connectedelement = aadl2_connectedelement;
    }

}