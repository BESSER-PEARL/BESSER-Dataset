





import java.util.List;
import java.util.ArrayList;

public class model_Receive extends PartnerActivity {

    private String createInstance;





    private model_MessageExchange model_messageexchange;




    private model_FromParts model_fromparts;




    private model_Variable model_variable;


    public model_Receive(
        String createInstance    ) {
        super(
        );
        this.createInstance = createInstance;
    }


    public String getCreateinstance() {
        return createInstance;
    }

    public void setCreateinstance(String createInstance) {
        this.createInstance = createInstance;
    }

    public model_MessageExchange getModel_messageexchange() {
        return model_messageexchange;
    }

    public void setModel_messageexchange(model_MessageExchange model_messageexchange) {
        this.model_messageexchange = model_messageexchange;
    }
    public model_FromParts getModel_fromparts() {
        return model_fromparts;
    }

    public void setModel_fromparts(model_FromParts model_fromparts) {
        this.model_fromparts = model_fromparts;
    }
    public model_Variable getModel_variable() {
        return model_variable;
    }

    public void setModel_variable(model_Variable model_variable) {
        this.model_variable = model_variable;
    }

}