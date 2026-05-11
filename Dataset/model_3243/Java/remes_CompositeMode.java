





import java.util.List;
import java.util.ArrayList;

public class remes_CompositeMode extends Mode {






    private remes_CompositeEntryPoint remes_compositeentrypoint;




    private List<remes_SubMode> remes_submodes;




    private remes_ConditionalConnector remes_conditionalconnector;




    private remes_CompositeExitPoint remes_compositeexitpoint;




    private remes_InitPoint remes_initpoint;




    private remes_SubMode remes_submode;




    private remes_CompositeExitPoint remes_compositeexitpoint;




    private remes_CompositeEntryPoint remes_compositeentrypoint;




    private List<remes_ConditionalConnector> remes_conditionalconnectors;


    public remes_CompositeMode(
    ) {
        super(
        );
        this.remes_submodes = new ArrayList<>();
        this.remes_conditionalconnectors = new ArrayList<>();
    }

    public remes_CompositeMode(
        ArrayList<remes_SubMode> remes_submodes,        ArrayList<remes_ConditionalConnector> remes_conditionalconnectors    ) {
        this.remes_submodes = remes_submodes;
        this.remes_conditionalconnectors = remes_conditionalconnectors;
    }


    public remes_CompositeEntryPoint getRemes_compositeentrypoint() {
        return remes_compositeentrypoint;
    }

    public void setRemes_compositeentrypoint(remes_CompositeEntryPoint remes_compositeentrypoint) {
        this.remes_compositeentrypoint = remes_compositeentrypoint;
    }
    public List<remes_SubMode> getRemes_submodes() {
        return remes_submodes;
    }

    public void addRemes_submode(Remes_submode remes_submode) {
        this.remes_submodes.add(remes_submode);
    }
    public remes_ConditionalConnector getRemes_conditionalconnector() {
        return remes_conditionalconnector;
    }

    public void setRemes_conditionalconnector(remes_ConditionalConnector remes_conditionalconnector) {
        this.remes_conditionalconnector = remes_conditionalconnector;
    }
    public remes_CompositeExitPoint getRemes_compositeexitpoint() {
        return remes_compositeexitpoint;
    }

    public void setRemes_compositeexitpoint(remes_CompositeExitPoint remes_compositeexitpoint) {
        this.remes_compositeexitpoint = remes_compositeexitpoint;
    }
    public remes_InitPoint getRemes_initpoint() {
        return remes_initpoint;
    }

    public void setRemes_initpoint(remes_InitPoint remes_initpoint) {
        this.remes_initpoint = remes_initpoint;
    }
    public remes_SubMode getRemes_submode() {
        return remes_submode;
    }

    public void setRemes_submode(remes_SubMode remes_submode) {
        this.remes_submode = remes_submode;
    }
    public remes_CompositeExitPoint getRemes_compositeexitpoint() {
        return remes_compositeexitpoint;
    }

    public void setRemes_compositeexitpoint(remes_CompositeExitPoint remes_compositeexitpoint) {
        this.remes_compositeexitpoint = remes_compositeexitpoint;
    }
    public remes_CompositeEntryPoint getRemes_compositeentrypoint() {
        return remes_compositeentrypoint;
    }

    public void setRemes_compositeentrypoint(remes_CompositeEntryPoint remes_compositeentrypoint) {
        this.remes_compositeentrypoint = remes_compositeentrypoint;
    }
    public List<remes_ConditionalConnector> getRemes_conditionalconnectors() {
        return remes_conditionalconnectors;
    }

    public void addRemes_conditionalconnector(Remes_conditionalconnector remes_conditionalconnector) {
        this.remes_conditionalconnectors.add(remes_conditionalconnector);
    }

}