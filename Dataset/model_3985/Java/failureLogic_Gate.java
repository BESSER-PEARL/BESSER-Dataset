





import java.util.List;
import java.util.ArrayList;

public class failureLogic_Gate extends Cause {

    private String gateType;





    private List<failureLogic_Cause> failurelogic_causes;


    public failureLogic_Gate(
        String gateType    ) {
        super(
        );
        this.gateType = gateType;
        this.failurelogic_causes = new ArrayList<>();
    }

    public failureLogic_Gate(
        String gateType        ArrayList<failureLogic_Cause> failurelogic_causes    ) {
        this.gateType = gateType;
        this.failurelogic_causes = failurelogic_causes;
    }

    public String getGatetype() {
        return gateType;
    }

    public void setGatetype(String gateType) {
        this.gateType = gateType;
    }

    public List<failureLogic_Cause> getFailurelogic_causes() {
        return failurelogic_causes;
    }

    public void addFailurelogic_cause(Failurelogic_cause failurelogic_cause) {
        this.failurelogic_causes.add(failurelogic_cause);
    }

}