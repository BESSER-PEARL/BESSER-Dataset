





import java.util.List;
import java.util.ArrayList;

public class uma_MethodElement extends PackageableElement {

    private String guid;
    private String suppressed;
    private String briefDescription;
    private String orderingGuide;



    public uma_MethodElement(
        String guid,        String suppressed,        String briefDescription,        String orderingGuide    ) {
        super(
        );
        this.guid = guid;
        this.suppressed = suppressed;
        this.briefDescription = briefDescription;
        this.orderingGuide = orderingGuide;
    }


    public String getGuid() {
        return guid;
    }

    public void setGuid(String guid) {
        this.guid = guid;
    }
    public String getSuppressed() {
        return suppressed;
    }

    public void setSuppressed(String suppressed) {
        this.suppressed = suppressed;
    }
    public String getBriefdescription() {
        return briefDescription;
    }

    public void setBriefdescription(String briefDescription) {
        this.briefDescription = briefDescription;
    }
    public String getOrderingguide() {
        return orderingGuide;
    }

    public void setOrderingguide(String orderingGuide) {
        this.orderingGuide = orderingGuide;
    }


}