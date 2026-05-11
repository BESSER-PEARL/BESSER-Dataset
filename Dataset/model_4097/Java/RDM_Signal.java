





import java.util.List;
import java.util.ArrayList;

public class RDM_Signal extends RDMElement {

    private String allowedSpeed;





    private RDM_ConnectionPoint rdm_connectionpoint;




    private RDM_ConnectionPoint rdm_connectionpoint;


    public RDM_Signal(
        String allowedSpeed    ) {
        super(
        );
        this.allowedSpeed = allowedSpeed;
    }


    public String getAllowedspeed() {
        return allowedSpeed;
    }

    public void setAllowedspeed(String allowedSpeed) {
        this.allowedSpeed = allowedSpeed;
    }

    public RDM_ConnectionPoint getRdm_connectionpoint() {
        return rdm_connectionpoint;
    }

    public void setRdm_connectionpoint(RDM_ConnectionPoint rdm_connectionpoint) {
        this.rdm_connectionpoint = rdm_connectionpoint;
    }
    public RDM_ConnectionPoint getRdm_connectionpoint() {
        return rdm_connectionpoint;
    }

    public void setRdm_connectionpoint(RDM_ConnectionPoint rdm_connectionpoint) {
        this.rdm_connectionpoint = rdm_connectionpoint;
    }

}