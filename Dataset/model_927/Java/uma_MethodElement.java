





import java.util.List;
import java.util.ArrayList;

public class uma_MethodElement extends PackageableElement {

    private String guid;
    private String orderingGuide;
    private String suppressed;
    private String presentationName;
    private String briefDescription;





    private List<uma_MethodElementProperty> uma_methodelementpropertys;


    public uma_MethodElement(
        String guid,        String orderingGuide,        String suppressed,        String presentationName,        String briefDescription    ) {
        super(
        );
        this.guid = guid;
        this.orderingGuide = orderingGuide;
        this.suppressed = suppressed;
        this.presentationName = presentationName;
        this.briefDescription = briefDescription;
        this.uma_methodelementpropertys = new ArrayList<>();
    }

    public uma_MethodElement(
        String guid,        String orderingGuide,        String suppressed,        String presentationName,        String briefDescription        ArrayList<uma_MethodElementProperty> uma_methodelementpropertys    ) {
        this.guid = guid;
        this.orderingGuide = orderingGuide;
        this.suppressed = suppressed;
        this.presentationName = presentationName;
        this.briefDescription = briefDescription;
        this.uma_methodelementpropertys = uma_methodelementpropertys;
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
    public String getBriefdescription() {
        return briefDescription;
    }

    public void setBriefdescription(String briefDescription) {
        this.briefDescription = briefDescription;
    }

    public List<uma_MethodElementProperty> getUma_methodelementpropertys() {
        return uma_methodelementpropertys;
    }

    public void addUma_methodelementproperty(Uma_methodelementproperty uma_methodelementproperty) {
        this.uma_methodelementpropertys.add(uma_methodelementproperty);
    }

}