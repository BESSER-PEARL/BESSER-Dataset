





import java.util.List;
import java.util.ArrayList;

public class core_MatchTrace extends Expression {

    private String cardinality;





    private core_TraceDefinition core_tracedefinition;


    public core_MatchTrace(
        String cardinality    ) {
        super(
        );
        this.cardinality = cardinality;
    }


    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }

    public core_TraceDefinition getCore_tracedefinition() {
        return core_tracedefinition;
    }

    public void setCore_tracedefinition(core_TraceDefinition core_tracedefinition) {
        this.core_tracedefinition = core_tracedefinition;
    }

}