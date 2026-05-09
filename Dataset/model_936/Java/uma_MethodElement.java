





import java.util.List;
import java.util.ArrayList;

public class uma_MethodElement extends PackageableElement {

    private String id;
    private String suppressed;
    private String briefDescription;
    private String group;
    private String orderingGuide;
    private String presentationName;



    public uma_MethodElement(
        String id,        String suppressed,        String briefDescription,        String group,        String orderingGuide,        String presentationName    ) {
        super(
        );
        this.id = id;
        this.suppressed = suppressed;
        this.briefDescription = briefDescription;
        this.group = group;
        this.orderingGuide = orderingGuide;
        this.presentationName = presentationName;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getOrderingguide() {
        return orderingGuide;
    }

    public void setOrderingguide(String orderingGuide) {
        this.orderingGuide = orderingGuide;
    }
    public String getPresentationname() {
        return presentationName;
    }

    public void setPresentationname(String presentationName) {
        this.presentationName = presentationName;
    }


}