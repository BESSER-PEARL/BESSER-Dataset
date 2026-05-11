





import java.util.List;
import java.util.ArrayList;

public class di_BPMNShape extends LabeledShape {

    private boolean isMessageVisible;
    private boolean isExpanded;
    private String participantBandKind;
    private boolean isHorizontal;
    private boolean isMarkerVisible;





    private di_DocumentRoot di_documentroot;




    private di_BPMNShape di_bpmnshape;




    private di_BPMNLabel di_bpmnlabel;


    public di_BPMNShape(
        boolean isMessageVisible,        boolean isExpanded,        String participantBandKind,        boolean isHorizontal,        boolean isMarkerVisible    ) {
        super(
        );
        this.isMessageVisible = isMessageVisible;
        this.isExpanded = isExpanded;
        this.participantBandKind = participantBandKind;
        this.isHorizontal = isHorizontal;
        this.isMarkerVisible = isMarkerVisible;
    }


    public boolean getIsmessagevisible() {
        return isMessageVisible;
    }

    public void setIsmessagevisible(boolean isMessageVisible) {
        this.isMessageVisible = isMessageVisible;
    }
    public boolean getIsexpanded() {
        return isExpanded;
    }

    public void setIsexpanded(boolean isExpanded) {
        this.isExpanded = isExpanded;
    }
    public String getParticipantbandkind() {
        return participantBandKind;
    }

    public void setParticipantbandkind(String participantBandKind) {
        this.participantBandKind = participantBandKind;
    }
    public boolean getIshorizontal() {
        return isHorizontal;
    }

    public void setIshorizontal(boolean isHorizontal) {
        this.isHorizontal = isHorizontal;
    }
    public boolean getIsmarkervisible() {
        return isMarkerVisible;
    }

    public void setIsmarkervisible(boolean isMarkerVisible) {
        this.isMarkerVisible = isMarkerVisible;
    }

    public di_DocumentRoot getDi_documentroot() {
        return di_documentroot;
    }

    public void setDi_documentroot(di_DocumentRoot di_documentroot) {
        this.di_documentroot = di_documentroot;
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