





import java.util.List;
import java.util.ArrayList;

public class rdal_ReferencedDesignElements extends IdentifiedElement {

    private String agregationType;





    private rdal_DesignElementReference rdal_designelementreference;




    private List<rdal_DesignElementReference> rdal_designelementreferences;




    private rdal_TraceableToDesignElementsElement rdal_traceabletodesignelementselement;


    public rdal_ReferencedDesignElements(
        String agregationType    ) {
        super(
        );
        this.agregationType = agregationType;
        this.rdal_designelementreferences = new ArrayList<>();
    }

    public rdal_ReferencedDesignElements(
        String agregationType        ArrayList<rdal_DesignElementReference> rdal_designelementreferences    ) {
        this.agregationType = agregationType;
        this.rdal_designelementreferences = rdal_designelementreferences;
    }

    public String getAgregationtype() {
        return agregationType;
    }

    public void setAgregationtype(String agregationType) {
        this.agregationType = agregationType;
    }

    public rdal_DesignElementReference getRdal_designelementreference() {
        return rdal_designelementreference;
    }

    public void setRdal_designelementreference(rdal_DesignElementReference rdal_designelementreference) {
        this.rdal_designelementreference = rdal_designelementreference;
    }
    public List<rdal_DesignElementReference> getRdal_designelementreferences() {
        return rdal_designelementreferences;
    }

    public void addRdal_designelementreference(Rdal_designelementreference rdal_designelementreference) {
        this.rdal_designelementreferences.add(rdal_designelementreference);
    }
    public rdal_TraceableToDesignElementsElement getRdal_traceabletodesignelementselement() {
        return rdal_traceabletodesignelementselement;
    }

    public void setRdal_traceabletodesignelementselement(rdal_TraceableToDesignElementsElement rdal_traceabletodesignelementselement) {
        this.rdal_traceabletodesignelementselement = rdal_traceabletodesignelementselement;
    }

}