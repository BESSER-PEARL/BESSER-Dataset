





import java.util.List;
import java.util.ArrayList;

public class uma_MethodElement extends PackageableElement {

    private String suppressed;
    private String guid;
    private String orderingGuide;
    private String briefDescription;



    public uma_MethodElement(
        String suppressed,        String guid,        String orderingGuide,        String briefDescription    ) {
        super(
        );
        this.suppressed = suppressed;
        this.guid = guid;
        this.orderingGuide = orderingGuide;
        this.briefDescription = briefDescription;
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
    public String getOrderingguide() {
        return orderingGuide;
    }

    public void setOrderingguide(String orderingGuide) {
        this.orderingGuide = orderingGuide;
    }
    public String getBriefdescription() {
        return briefDescription;
    }

    public void setBriefdescription(String briefDescription) {
        this.briefDescription = briefDescription;
    }


}