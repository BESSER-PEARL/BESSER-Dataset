





import java.util.List;
import java.util.ArrayList;

public class PiServiceComposition_Action extends ExecutableNode {

    private String type;





    private PiServiceComposition_ServiceActivity piservicecomposition_serviceactivity;


    public PiServiceComposition_Action(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public PiServiceComposition_ServiceActivity getPiservicecomposition_serviceactivity() {
        return piservicecomposition_serviceactivity;
    }

    public void setPiservicecomposition_serviceactivity(PiServiceComposition_ServiceActivity piservicecomposition_serviceactivity) {
        this.piservicecomposition_serviceactivity = piservicecomposition_serviceactivity;
    }

}