





import java.util.List;
import java.util.ArrayList;

public class uma_MethodElement extends PackageableElement {

    private String orderingGuide;
    private String briefDescription;
    private String id;
    private String group;
    private String suppressed;
    private String presentationName;





    private List<uma_MethodElementProperty> uma_methodelementpropertys;


    public uma_MethodElement(
        String orderingGuide,        String briefDescription,        String id,        String group,        String suppressed,        String presentationName    ) {
        super(
        );
        this.orderingGuide = orderingGuide;
        this.briefDescription = briefDescription;
        this.id = id;
        this.group = group;
        this.suppressed = suppressed;
        this.presentationName = presentationName;
        this.uma_methodelementpropertys = new ArrayList<>();
    }

    public uma_MethodElement(
        String orderingGuide,        String briefDescription,        String id,        String group,        String suppressed,        String presentationName        ArrayList<uma_MethodElementProperty> uma_methodelementpropertys    ) {
        this.orderingGuide = orderingGuide;
        this.briefDescription = briefDescription;
        this.id = id;
        this.group = group;
        this.suppressed = suppressed;
        this.presentationName = presentationName;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
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

    public List<uma_MethodElementProperty> getUma_methodelementpropertys() {
        return uma_methodelementpropertys;
    }

    public void addUma_methodelementproperty(Uma_methodelementproperty uma_methodelementproperty) {
        this.uma_methodelementpropertys.add(uma_methodelementproperty);
    }

}