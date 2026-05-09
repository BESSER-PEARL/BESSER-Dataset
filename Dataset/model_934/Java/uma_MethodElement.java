





import java.util.List;
import java.util.ArrayList;

public class uma_MethodElement extends PackageableElement {

    private String presentationName;
    private String id;
    private String briefDescription;
    private String orderingGuide;
    private String suppressed;
    private String group;



    public uma_MethodElement(
        String presentationName,        String id,        String briefDescription,        String orderingGuide,        String suppressed,        String group    ) {
        super(
        );
        this.presentationName = presentationName;
        this.id = id;
        this.briefDescription = briefDescription;
        this.orderingGuide = orderingGuide;
        this.suppressed = suppressed;
        this.group = group;
    }


    public String getPresentationname() {
        return presentationName;
    }

    public void setPresentationname(String presentationName) {
        this.presentationName = presentationName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public String getSuppressed() {
        return suppressed;
    }

    public void setSuppressed(String suppressed) {
        this.suppressed = suppressed;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }


}