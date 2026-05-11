





import java.util.List;
import java.util.ArrayList;

public class di_BPMNShape extends LabeledShape {

    private boolean isExpanded;
    private boolean isHorizontal;
    private String participantBandKind;
    private boolean isMarkerVisible;
    private boolean isMessageVisible;





    private di_BPMNShape di_bpmnshape;




    private di_BPMNLabel di_bpmnlabel;


    public di_BPMNShape(
        boolean isExpanded,        boolean isHorizontal,        String participantBandKind,        boolean isMarkerVisible,        boolean isMessageVisible    ) {
        super(
        );
        this.isExpanded = isExpanded;
        this.isHorizontal = isHorizontal;
        this.participantBandKind = participantBandKind;
        this.isMarkerVisible = isMarkerVisible;
        this.isMessageVisible = isMessageVisible;
    }


    public boolean getIsexpanded() {
        return isExpanded;
    }

    public void setIsexpanded(boolean isExpanded) {
        this.isExpanded = isExpanded;
    }
    public boolean getIshorizontal() {
        return isHorizontal;
    }

    public void setIshorizontal(boolean isHorizontal) {
        this.isHorizontal = isHorizontal;
    }
    public String getParticipantbandkind() {
        return participantBandKind;
    }

    public void setParticipantbandkind(String participantBandKind) {
        this.participantBandKind = participantBandKind;
    }
    public boolean getIsmarkervisible() {
        return isMarkerVisible;
    }

    public void setIsmarkervisible(boolean isMarkerVisible) {
        this.isMarkerVisible = isMarkerVisible;
    }
    public boolean getIsmessagevisible() {
        return isMessageVisible;
    }

    public void setIsmessagevisible(boolean isMessageVisible) {
        this.isMessageVisible = isMessageVisible;
    }

    public di_BPMNShape getDi_bpmnshape() {
        return di_bpmnshape;
    }

    public void setDi_bpmnshape(di_BPMNShape di_bpmnshape) {
        this.di_bpmnshape = di_bpmnshape;
    }
    public di_BPMNLabel getDi_bpmnlabel() {
        return di_bpmnlabel;
    }

    public void setDi_bpmnlabel(di_BPMNLabel di_bpmnlabel) {
        this.di_bpmnlabel = di_bpmnlabel;
    }

}