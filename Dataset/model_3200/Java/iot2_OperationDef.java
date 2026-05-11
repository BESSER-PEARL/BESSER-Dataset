





import java.util.List;
import java.util.ArrayList;

public class iot2_OperationDef extends Contained, Typed {

    private String contexts;
    private boolean isOneway;





    private iot2_HWComponent iot2_hwcomponent;


    public iot2_OperationDef(
        String contexts,        boolean isOneway    ) {
        super(
        );
        this.contexts = contexts;
        this.isOneway = isOneway;
    }


    public String getContexts() {
        return contexts;
    }

    public void setContexts(String contexts) {
        this.contexts = contexts;
    }
    public boolean getIsoneway() {
        return isOneway;
    }

    public void setIsoneway(boolean isOneway) {
        this.isOneway = isOneway;
    }

    public iot2_HWComponent getIot2_hwcomponent() {
        return iot2_hwcomponent;
    }

    public void setIot2_hwcomponent(iot2_HWComponent iot2_hwcomponent) {
        this.iot2_hwcomponent = iot2_hwcomponent;
    }

}