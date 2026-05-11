





import java.util.List;
import java.util.ArrayList;

public class RDM_Train extends RDMElement {

    private String headingSpeed;
    private String maxSpeed;





    private RDM_Route rdm_route;


    public RDM_Train(
        String headingSpeed,        String maxSpeed    ) {
        super(
        );
        this.headingSpeed = headingSpeed;
        this.maxSpeed = maxSpeed;
    }


    public String getHeadingspeed() {
        return headingSpeed;
    }

    public void setHeadingspeed(String headingSpeed) {
        this.headingSpeed = headingSpeed;
    }
    public String getMaxspeed() {
        return maxSpeed;
    }

    public void setMaxspeed(String maxSpeed) {
        this.maxSpeed = maxSpeed;
    }

    public RDM_Route getRdm_route() {
        return rdm_route;
    }

    public void setRdm_route(RDM_Route rdm_route) {
        this.rdm_route = rdm_route;
    }

}