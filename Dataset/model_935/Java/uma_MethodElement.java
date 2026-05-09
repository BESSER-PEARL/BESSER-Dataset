





import java.util.List;
import java.util.ArrayList;

public class uma_MethodElement extends PackageableElement {

    private String suppressed;
    private String briefDescription;
    private String id;
    private String orderingGuide;
    private String group;
    private String presentationName;



    public uma_MethodElement(
        String suppressed,        String briefDescription,        String id,        String orderingGuide,        String group,        String presentationName    ) {
        super(
        );
        this.suppressed = suppressed;
        this.briefDescription = briefDescription;
        this.id = id;
        this.orderingGuide = orderingGuide;
        this.group = group;
        this.presentationName = presentationName;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getOrderingguide() {
        return orderingGuide;
    }

    public void setOrderingguide(String orderingGuide) {
        this.orderingGuide = orderingGuide;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getPresentationname() {
        return presentationName;
    }

    public void setPresentationname(String presentationName) {
        this.presentationName = presentationName;
    }


}