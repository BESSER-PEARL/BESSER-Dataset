





import java.util.List;
import java.util.ArrayList;

public class rdal_DesignElementReference extends IdentifiedElement {

    private String evaluationResult;





    private rdal_TraceableToDesignElementsElement rdal_traceabletodesignelementselement;


    public rdal_DesignElementReference(
        String evaluationResult    ) {
        super(
        );
        this.evaluationResult = evaluationResult;
    }


    public String getEvaluationresult() {
        return evaluationResult;
    }

    public void setEvaluationresult(String evaluationResult) {
        this.evaluationResult = evaluationResult;
    }

    public rdal_TraceableToDesignElementsElement getRdal_traceabletodesignelementselement() {
        return rdal_traceabletodesignelementselement;
    }

    public void setRdal_traceabletodesignelementselement(rdal_TraceableToDesignElementsElement rdal_traceabletodesignelementselement) {
        this.rdal_traceabletodesignelementselement = rdal_traceabletodesignelementselement;
    }

}