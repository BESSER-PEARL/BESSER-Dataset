





import java.util.List;
import java.util.ArrayList;

public class UML2_Port extends Property {

    private boolean isService;
    private boolean isBehavior;





    private UML2_Trigger uml2_trigger;




    private UML2_Port uml2_port;


    public UML2_Port(
        boolean isService,        boolean isBehavior    ) {
        super(
        );
        this.isService = isService;
        this.isBehavior = isBehavior;
    }


    public boolean getIsservice() {
        return isService;
    }

    public void setIsservice(boolean isService) {
        this.isService = isService;
    }
    public boolean getIsbehavior() {
        return isBehavior;
    }

    public void setIsbehavior(boolean isBehavior) {
        this.isBehavior = isBehavior;
    }

    public UML2_Trigger getUml2_trigger() {
        return uml2_trigger;
    }

    public void setUml2_trigger(UML2_Trigger uml2_trigger) {
        this.uml2_trigger = uml2_trigger;
    }
    public UML2_Port getUml2_port() {
        return uml2_port;
    }

    public void setUml2_port(UML2_Port uml2_port) {
        this.uml2_port = uml2_port;
    }

}