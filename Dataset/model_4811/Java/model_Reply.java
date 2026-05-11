





import java.util.List;
import java.util.ArrayList;

public class model_Reply extends Activity, PartnerActivity {

    private String faultName;





    private model_MessageExchange model_messageexchange;




    private model_Variable model_variable;




    private model_ToParts model_toparts;


    public model_Reply(
        String faultName    ) {
        super(
        );
        this.faultName = faultName;
    }


    public String getFaultname() {
        return faultName;
    }

    public void setFaultname(String faultName) {
        this.faultName = faultName;
    }

    public model_MessageExchange getModel_messageexchange() {
        return model_messageexchange;
    }

    public void setModel_messageexchange(model_MessageExchange model_messageexchange) {
        this.model_messageexchange = model_messageexchange;
    }
    public model_Variable getModel_variable() {
        return model_variable;
    }

    public void setModel_variable(model_Variable model_variable) {
        this.model_variable = model_variable;
    }
    public model_ToParts getModel_toparts() {
        return model_toparts;
    }

    public void setModel_toparts(model_ToParts model_toparts) {
        this.model_toparts = model_toparts;
    }

}