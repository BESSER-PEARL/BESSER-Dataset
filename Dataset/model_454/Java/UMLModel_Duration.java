





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Duration extends ValueSpecification {

    private String observation;
    private String expr;



    public UMLModel_Duration(
        String observation,        String expr    ) {
        super(
        );
        this.observation = observation;
        this.expr = expr;
    }


    public String getObservation() {
        return observation;
    }

    public void setObservation(String observation) {
        this.observation = observation;
    }
    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }


}