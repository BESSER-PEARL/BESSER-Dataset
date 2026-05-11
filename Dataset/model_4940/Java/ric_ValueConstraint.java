





import java.util.List;
import java.util.ArrayList;

public class ric_ValueConstraint extends FormControlConstraint {

    private String logicalOperator;
    private String matchingOperator;
    private String matchingValue;





    private ric_FormControl ric_formcontrol;


    public ric_ValueConstraint(
        String logicalOperator,        String matchingOperator,        String matchingValue    ) {
        super(
        );
        this.logicalOperator = logicalOperator;
        this.matchingOperator = matchingOperator;
        this.matchingValue = matchingValue;
    }


    public String getLogicaloperator() {
        return logicalOperator;
    }

    public void setLogicaloperator(String logicalOperator) {
        this.logicalOperator = logicalOperator;
    }
    public String getMatchingoperator() {
        return matchingOperator;
    }

    public void setMatchingoperator(String matchingOperator) {
        this.matchingOperator = matchingOperator;
    }
    public String getMatchingvalue() {
        return matchingValue;
    }

    public void setMatchingvalue(String matchingValue) {
        this.matchingValue = matchingValue;
    }

    public ric_FormControl getRic_formcontrol() {
        return ric_formcontrol;
    }

    public void setRic_formcontrol(ric_FormControl ric_formcontrol) {
        this.ric_formcontrol = ric_formcontrol;
    }

}