





import java.util.List;
import java.util.ArrayList;

public class uma_MethodElement extends PackageableElement {

    private String orderingGuide;
    private String guid;
    private String suppressed;
    private String presentationName;
    private String briefDescription;





    private List<uma_Constraint> uma_constraints;




    private uma_UMASemanticModelBridge uma_umasemanticmodelbridge;




    private List<uma_MethodElementProperty> uma_methodelementpropertys;


    public uma_MethodElement(
        String orderingGuide,        String guid,        String suppressed,        String presentationName,        String briefDescription    ) {
        super(
        );
        this.orderingGuide = orderingGuide;
        this.guid = guid;
        this.suppressed = suppressed;
        this.presentationName = presentationName;
        this.briefDescription = briefDescription;
        this.uma_constraints = new ArrayList<>();
        this.uma_methodelementpropertys = new ArrayList<>();
    }

    public uma_MethodElement(
        String orderingGuide,        String guid,        String suppressed,        String presentationName,        String briefDescription        ArrayList<uma_Constraint> uma_constraints,        ArrayList<uma_MethodElementProperty> uma_methodelementpropertys    ) {
        this.orderingGuide = orderingGuide;
        this.guid = guid;
        this.suppressed = suppressed;
        this.presentationName = presentationName;
        this.briefDescription = briefDescription;
        this.uma_constraints = uma_constraints;
        this.uma_methodelementpropertys = uma_methodelementpropertys;
    }

    public String getOrderingguide() {
        return orderingGuide;
    }

    public void setOrderingguide(String orderingGuide) {
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

    public List<uma_Constraint> getUma_constraints() {
        return uma_constraints;
    }

    public void addUma_constraint(Uma_constraint uma_constraint) {
        this.uma_constraints.add(uma_constraint);
    }
    public uma_UMASemanticModelBridge getUma_umasemanticmodelbridge() {
        return uma_umasemanticmodelbridge;
    }

    public void setUma_umasemanticmodelbridge(uma_UMASemanticModelBridge uma_umasemanticmodelbridge) {
        this.uma_umasemanticmodelbridge = uma_umasemanticmodelbridge;
    }
    public List<uma_MethodElementProperty> getUma_methodelementpropertys() {
        return uma_methodelementpropertys;
    }

    public void addUma_methodelementproperty(Uma_methodelementproperty uma_methodelementproperty) {
        this.uma_methodelementpropertys.add(uma_methodelementproperty);
    }

}