





import java.util.List;
import java.util.ArrayList;

public class model_Scope extends Activity {

    private String exitOnStandardFault;
    private String isolated;





    private model_CompensationHandler model_compensationhandler;




    private model_Activity model_activity;




    private model_PartnerLinks model_partnerlinks;




    private model_CorrelationSets model_correlationsets;




    private model_FaultHandler model_faulthandler;




    private model_Variables model_variables;




    private model_EventHandler model_eventhandler;




    private model_TerminationHandler model_terminationhandler;




    private model_MessageExchanges model_messageexchanges;


    public model_Scope(
        String exitOnStandardFault,        String isolated    ) {
        super(
        );
        this.exitOnStandardFault = exitOnStandardFault;
        this.isolated = isolated;
    }


    public String getExitonstandardfault() {
        return exitOnStandardFault;
    }

    public void setExitonstandardfault(String exitOnStandardFault) {
        this.exitOnStandardFault = exitOnStandardFault;
    }
    public String getIsolated() {
        return isolated;
    }

    public void setIsolated(String isolated) {
        this.isolated = isolated;
    }

    public model_CompensationHandler getModel_compensationhandler() {
        return model_compensationhandler;
    }

    public void setModel_compensationhandler(model_CompensationHandler model_compensationhandler) {
        this.model_compensationhandler = model_compensationhandler;
    }
    public model_Activity getModel_activity() {
        return model_activity;
    }

    public void setModel_activity(model_Activity model_activity) {
        this.model_activity = model_activity;
    }
    public model_PartnerLinks getModel_partnerlinks() {
        return model_partnerlinks;
    }

    public void setModel_partnerlinks(model_PartnerLinks model_partnerlinks) {
        this.model_partnerlinks = model_partnerlinks;
    }
    public model_CorrelationSets getModel_correlationsets() {
        return model_correlationsets;
    }

    public void setModel_correlationsets(model_CorrelationSets model_correlationsets) {
        this.model_correlationsets = model_correlationsets;
    }
    public model_FaultHandler getModel_faulthandler() {
        return model_faulthandler;
    }

    public void setModel_faulthandler(model_FaultHandler model_faulthandler) {
        this.model_faulthandler = model_faulthandler;
    }
    public model_Variables getModel_variables() {
        return model_variables;
    }

    public void setModel_variables(model_Variables model_variables) {
        this.model_variables = model_variables;
    }
    public model_EventHandler getModel_eventhandler() {
        return model_eventhandler;
    }

    public void setModel_eventhandler(model_EventHandler model_eventhandler) {
        this.model_eventhandler = model_eventhandler;
    }
    public model_TerminationHandler getModel_terminationhandler() {
        return model_terminationhandler;
    }

    public void setModel_terminationhandler(model_TerminationHandler model_terminationhandler) {
        this.model_terminationhandler = model_terminationhandler;
    }
    public model_MessageExchanges getModel_messageexchanges() {
        return model_messageexchanges;
    }

    public void setModel_messageexchanges(model_MessageExchanges model_messageexchanges) {
        this.model_messageexchanges = model_messageexchanges;
    }

}