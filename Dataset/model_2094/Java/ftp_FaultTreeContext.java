





import java.util.List;
import java.util.ArrayList;

public class ftp_FaultTreeContext  {






    private List<ftp_Observation> ftp_observations;




    private ftp_ComposedComponent ftp_composedcomponent;


    public ftp_FaultTreeContext(
    ) {
        this.ftp_observations = new ArrayList<>();
    }

    public ftp_FaultTreeContext(
        ArrayList<ftp_Observation> ftp_observations    ) {
        this.ftp_observations = ftp_observations;
    }


    public List<ftp_Observation> getFtp_observations() {
        return ftp_observations;
    }

    public void addFtp_observation(Ftp_observation ftp_observation) {
        this.ftp_observations.add(ftp_observation);
    }
    public ftp_ComposedComponent getFtp_composedcomponent() {
        return ftp_composedcomponent;
    }

    public void setFtp_composedcomponent(ftp_ComposedComponent ftp_composedcomponent) {
        this.ftp_composedcomponent = ftp_composedcomponent;
    }

}