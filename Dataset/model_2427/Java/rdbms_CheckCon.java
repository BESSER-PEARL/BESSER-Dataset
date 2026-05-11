





import java.util.List;
import java.util.ArrayList;

public class rdbms_CheckCon extends Constraints {

    private String checkCondition;



    public rdbms_CheckCon(
        String checkCondition    ) {
        super(
        );
        this.checkCondition = checkCondition;
    }


    public String getCheckcondition() {
        return checkCondition;
    }

    public void setCheckcondition(String checkCondition) {
        this.checkCondition = checkCondition;
    }


}