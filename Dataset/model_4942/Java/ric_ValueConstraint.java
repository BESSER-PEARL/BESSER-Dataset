





import java.util.List;
import java.util.ArrayList;

public class ric_ValueConstraint extends FormControlConstraint {

    private String matchingValue;
    private String logicalOperator;
    private String matchingOperator;





    private ric_FormControl ric_formcontrol;


    public ric_ValueConstraint(
        String matchingValue,        String logicalOperator,        String matchingOperator    ) {
        super(
        );
        this.matchingValue = matchingValue;
        this.logicalOperator = logicalOperator;
        this.matchingOperator = matchingOperator;
    }


    public String getMatchingvalue() {
        return matchingValue;
    }

    public void setMatchingvalue(String matchingValue) {
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

    public ric_FormControl getRic_formcontrol() {
        return ric_formcontrol;
    }

    public void setRic_formcontrol(ric_FormControl ric_formcontrol) {
        this.ric_formcontrol = ric_formcontrol;
    }

}