





import java.util.List;
import java.util.ArrayList;

public class uma_MethodElement extends PackageableElement {

    private String orderingGuide;
    private String suppressed;
    private String guid;
    private String presentationName;
    private String briefDescription;





    private uma_UMASemanticModelBridge uma_umasemanticmodelbridge;


    public uma_MethodElement(
        String orderingGuide,        String suppressed,        String guid,        String presentationName,        String briefDescription    ) {
        super(
        );
        this.orderingGuide = orderingGuide;
        this.suppressed = suppressed;
        this.guid = guid;
        this.presentationName = presentationName;
        this.briefDescription = briefDescription;
    }


    public String getOrderingguide() {
        return orderingGuide;
    }

    public void setOrderingguide(String orderingGuide) {
        this.orderingGuide = orderingGuide;
    }
    public String getSuppressed() {
        return suppressed;
    }

    public void setSuppressed(String suppressed) {
        this.suppressed = suppressed;
    }
    public String getGuid() {
        return guid;
    }

    public void setGuid(String guid) {
        this.guid = guid;
    }
    public String getPresentationname() {
        return presentationName;
    }

    public void setPresentationname(String presentationName) {
        this.presentationName = presentationName;
    }
    public String getBriefdescription() {
        return briefDescription;
    }

    public void setBriefdescription(String briefDescription) {
        this.briefDescription = briefDescription;
    }

    public uma_UMASemanticModelBridge getUma_umasemanticmodelbridge() {
        return uma_umasemanticmodelbridge;
    }

    public void setUma_umasemanticmodelbridge(uma_UMASemanticModelBridge uma_umasemanticmodelbridge) {
        this.uma_umasemanticmodelbridge = uma_umasemanticmodelbridge;
    }

}