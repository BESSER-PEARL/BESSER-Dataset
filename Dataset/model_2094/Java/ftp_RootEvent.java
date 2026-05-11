





import java.util.List;
import java.util.ArrayList;

public class ftp_RootEvent extends FTNode {

    private String observation;



    public ftp_RootEvent(
        String observation    ) {
        super(
        );
        this.observation = observation;
    }


    public String getObservation() {
        return observation;
    }

    public void setObservation(String observation) {
        this.observation = observation;
    }


}