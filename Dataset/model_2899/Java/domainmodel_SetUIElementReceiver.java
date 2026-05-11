





import java.util.List;
import java.util.ArrayList;

public class domainmodel_SetUIElementReceiver extends SetActionReceiver {

    private String uiKey;





    private domainmodel_AttachAction domainmodel_attachaction;




    private domainmodel_ValidateAction domainmodel_validateaction;




    private domainmodel_BindAction domainmodel_bindaction;




    private domainmodel_ViewElement domainmodel_viewelement;


    public domainmodel_SetUIElementReceiver(
        String uiKey    ) {
        super(
        );
        this.uiKey = uiKey;
    }


    public String getUikey() {
        return uiKey;
    }

    public void setUikey(String uiKey) {
        this.uiKey = uiKey;
    }

    public domainmodel_AttachAction getDomainmodel_attachaction() {
        return domainmodel_attachaction;
    }

    public void setDomainmodel_attachaction(domainmodel_AttachAction domainmodel_attachaction) {
        this.domainmodel_attachaction = domainmodel_attachaction;
    }
    public domainmodel_ValidateAction getDomainmodel_validateaction() {
        return domainmodel_validateaction;
    }

    public void setDomainmodel_validateaction(domainmodel_ValidateAction domainmodel_validateaction) {
        this.domainmodel_validateaction = domainmodel_validateaction;
    }
    public domainmodel_BindAction getDomainmodel_bindaction() {
        return domainmodel_bindaction;
    }

    public void setDomainmodel_bindaction(domainmodel_BindAction domainmodel_bindaction) {
        this.domainmodel_bindaction = domainmodel_bindaction;
    }
    public domainmodel_ViewElement getDomainmodel_viewelement() {
        return domainmodel_viewelement;
    }

    public void setDomainmodel_viewelement(domainmodel_ViewElement domainmodel_viewelement) {
        this.domainmodel_viewelement = domainmodel_viewelement;
    }

}