





import java.util.List;
import java.util.ArrayList;

public class uma_MethodElement extends PackageableElement {

    private String orderingGuide;
    private String briefDescription;
    private String suppressed;
    private String presentationName;
    private String guid;





    private List<uma_MethodElementProperty> uma_methodelementpropertys;


    public uma_MethodElement(
        String orderingGuide,        String briefDescription,        String suppressed,        String presentationName,        String guid    ) {
        super(
        );
        this.orderingGuide = orderingGuide;
        this.briefDescription = briefDescription;
        this.suppressed = suppressed;
        this.presentationName = presentationName;
        this.guid = guid;
        this.uma_methodelementpropertys = new ArrayList<>();
    }

    public uma_MethodElement(
        String orderingGuide,        String briefDescription,        String suppressed,        String presentationName,        String guid        ArrayList<uma_MethodElementProperty> uma_methodelementpropertys    ) {
        this.orderingGuide = orderingGuide;
        this.briefDescription = briefDescription;
        this.suppressed = suppressed;
        this.presentationName = presentationName;
        this.guid = guid;
        this.uma_methodelementpropertys = uma_methodelementpropertys;
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
    public String getSuppressed() {
        return suppressed;
    }

    public void setSuppressed(String suppressed) {
        this.suppressed = suppressed;
    }
    public String getPresentationname() {
        return presentationName;
    }

    public void setPresentationname(String presentationName) {
        this.presentationName = presentationName;
    }
    public String getGuid() {
        return guid;
    }

    public void setGuid(String guid) {
        this.guid = guid;
    }

    public List<uma_MethodElementProperty> getUma_methodelementpropertys() {
        return uma_methodelementpropertys;
    }

    public void addUma_methodelementproperty(Uma_methodelementproperty uma_methodelementproperty) {
        this.uma_methodelementpropertys.add(uma_methodelementproperty);
    }

}