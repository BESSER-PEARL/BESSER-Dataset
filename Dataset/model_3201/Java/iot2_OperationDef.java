





import java.util.List;
import java.util.ArrayList;

public class iot2_OperationDef extends Contained, Typed {

    private String contexts;
    private boolean isOneway;





    private List<iot2_ExceptionDef> iot2_exceptiondefs;




    private iot2_OpaqueAction iot2_opaqueaction;




    private iot2_HWComponent iot2_hwcomponent;


    public iot2_OperationDef(
        String contexts,        boolean isOneway    ) {
        super(
        );
        this.contexts = contexts;
        this.isOneway = isOneway;
        this.iot2_exceptiondefs = new ArrayList<>();
    }

    public iot2_OperationDef(
        String contexts,        boolean isOneway        ArrayList<iot2_ExceptionDef> iot2_exceptiondefs    ) {
        this.contexts = contexts;
        this.isOneway = isOneway;
        this.iot2_exceptiondefs = iot2_exceptiondefs;
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

    public List<iot2_ExceptionDef> getIot2_exceptiondefs() {
        return iot2_exceptiondefs;
    }

    public void addIot2_exceptiondef(Iot2_exceptiondef iot2_exceptiondef) {
        this.iot2_exceptiondefs.add(iot2_exceptiondef);
    }
    public iot2_OpaqueAction getIot2_opaqueaction() {
        return iot2_opaqueaction;
    }

    public void setIot2_opaqueaction(iot2_OpaqueAction iot2_opaqueaction) {
        this.iot2_opaqueaction = iot2_opaqueaction;
    }
    public iot2_HWComponent getIot2_hwcomponent() {
        return iot2_hwcomponent;
    }

    public void setIot2_hwcomponent(iot2_HWComponent iot2_hwcomponent) {
        this.iot2_hwcomponent = iot2_hwcomponent;
    }

}