





import java.util.List;
import java.util.ArrayList;

public class uma_MethodElement extends PackageableElement {

    private String orderingGuide;
    private String suppressed;
    private String guid;
    private String briefDescription;





    private List<uma_Constraint> uma_constraints;


    public uma_MethodElement(
        String orderingGuide,        String suppressed,        String guid,        String briefDescription    ) {
        super(
        );
        this.orderingGuide = orderingGuide;
        this.suppressed = suppressed;
        this.guid = guid;
        this.briefDescription = briefDescription;
        this.uma_constraints = new ArrayList<>();
    }

    public uma_MethodElement(
        String orderingGuide,        String suppressed,        String guid,        String briefDescription        ArrayList<uma_Constraint> uma_constraints    ) {
        this.orderingGuide = orderingGuide;
        this.suppressed = suppressed;
        this.guid = guid;
        this.briefDescription = briefDescription;
        this.uma_constraints = uma_constraints;
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

}