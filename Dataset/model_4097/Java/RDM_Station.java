





import java.util.List;
import java.util.ArrayList;

public class RDM_Station extends Section {






    private List<RDM_Signal> rdm_signals;




    private RDM_Train rdm_train;




    private RDM_Train rdm_train;


    public RDM_Station(
    ) {
        super(
        );
        this.rdm_signals = new ArrayList<>();
    }

    public RDM_Station(
        ArrayList<RDM_Signal> rdm_signals    ) {
        this.rdm_signals = rdm_signals;
    }


    public List<RDM_Signal> getRdm_signals() {
        return rdm_signals;
    }

    public void addRdm_signal(Rdm_signal rdm_signal) {
        this.rdm_signals.add(rdm_signal);
    }
    public RDM_Train getRdm_train() {
        return rdm_train;
    }

    public void setRdm_train(RDM_Train rdm_train) {
        this.rdm_train = rdm_train;
    }
    public RDM_Train getRdm_train() {
        return rdm_train;
    }

    public void setRdm_train(RDM_Train rdm_train) {
        this.rdm_train = rdm_train;
    }

}