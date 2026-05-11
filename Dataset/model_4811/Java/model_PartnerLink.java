





import java.util.List;
import java.util.ArrayList;

public class model_PartnerLink extends BPELExtensibleElement {

    private String name;
    private String initializePartnerRole;





    private model_OnMessage model_onmessage;




    private model_OnEvent model_onevent;


    public model_PartnerLink(
        String name,        String initializePartnerRole    ) {
        super(
        );
        this.name = name;
        this.initializePartnerRole = initializePartnerRole;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getInitializepartnerrole() {
        return initializePartnerRole;
    }

    public void setInitializepartnerrole(String initializePartnerRole) {
        this.initializePartnerRole = initializePartnerRole;
    }

    public model_OnMessage getModel_onmessage() {
        return model_onmessage;
    }

    public void setModel_onmessage(model_OnMessage model_onmessage) {
        this.model_onmessage = model_onmessage;
    }
    public model_OnEvent getModel_onevent() {
        return model_onevent;
    }

    public void setModel_onevent(model_OnEvent model_onevent) {
        this.model_onevent = model_onevent;
    }

}