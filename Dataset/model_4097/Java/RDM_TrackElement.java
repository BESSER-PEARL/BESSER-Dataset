





import java.util.List;
import java.util.ArrayList;

public class RDM_TrackElement extends RDMElement {






    private RDM_ConnectionPoint rdm_connectionpoint;




    private RDM_Train rdm_train;




    private RDM_Signal rdm_signal;




    private RDM_Train rdm_train;




    private RDM_RouteElement rdm_routeelement;




    private List<RDM_ConnectionPoint> rdm_connectionpoints;


    public RDM_TrackElement(
    ) {
        super(
        );
        this.rdm_connectionpoints = new ArrayList<>();
    }

    public RDM_TrackElement(
        ArrayList<RDM_ConnectionPoint> rdm_connectionpoints    ) {
        this.rdm_connectionpoints = rdm_connectionpoints;
    }


    public RDM_ConnectionPoint getRdm_connectionpoint() {
        return rdm_connectionpoint;
    }

    public void setRdm_connectionpoint(RDM_ConnectionPoint rdm_connectionpoint) {
        this.rdm_connectionpoint = rdm_connectionpoint;
    }
    public RDM_Train getRdm_train() {
        return rdm_train;
    }

    public void setRdm_train(RDM_Train rdm_train) {
        this.rdm_train = rdm_train;
    }
    public RDM_Signal getRdm_signal() {
        return rdm_signal;
    }

    public void setRdm_signal(RDM_Signal rdm_signal) {
        this.rdm_signal = rdm_signal;
    }
    public RDM_Train getRdm_train() {
        return rdm_train;
    }

    public void setRdm_train(RDM_Train rdm_train) {
        this.rdm_train = rdm_train;
    }
    public RDM_RouteElement getRdm_routeelement() {
        return rdm_routeelement;
    }

    public void setRdm_routeelement(RDM_RouteElement rdm_routeelement) {
        this.rdm_routeelement = rdm_routeelement;
    }
    public List<RDM_ConnectionPoint> getRdm_connectionpoints() {
        return rdm_connectionpoints;
    }

    public void addRdm_connectionpoint(Rdm_connectionpoint rdm_connectionpoint) {
        this.rdm_connectionpoints.add(rdm_connectionpoint);
    }

}