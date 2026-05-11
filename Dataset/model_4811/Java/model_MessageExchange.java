





import java.util.List;
import java.util.ArrayList;

public class model_MessageExchange extends BPELExtensibleElement {

    private String name;





    private model_OnEvent model_onevent;




    private model_MessageExchanges model_messageexchanges;




    private model_OnMessage model_onmessage;


    public model_MessageExchange(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_OnEvent getModel_onevent() {
        return model_onevent;
    }

    public void setModel_onevent(model_OnEvent model_onevent) {
        this.model_onevent = model_onevent;
    }
    public model_MessageExchanges getModel_messageexchanges() {
        return model_messageexchanges;
    }

    public void setModel_messageexchanges(model_MessageExchanges model_messageexchanges) {
        this.model_messageexchanges = model_messageexchanges;
    }
    public model_OnMessage getModel_onmessage() {
        return model_onmessage;
    }

    public void setModel_onmessage(model_OnMessage model_onmessage) {
        this.model_onmessage = model_onmessage;
    }

}