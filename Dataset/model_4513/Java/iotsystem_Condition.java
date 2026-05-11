





import java.util.List;
import java.util.ArrayList;

public class iotsystem_Condition  {

    private float expectedValue;
    private String relationalOperator;



    public iotsystem_Condition(
        float expectedValue,        String relationalOperator    ) {
        this.expectedValue = expectedValue;
        this.relationalOperator = relationalOperator;
    }


    public float getExpectedvalue() {
        return expectedValue;
    }

    public void setExpectedvalue(float expectedValue) {
        this.expectedValue = expectedValue;
    }
    public String getRelationaloperator() {
        return relationalOperator;
    }

    public void setRelationaloperator(String relationalOperator) {
        this.relationalOperator = relationalOperator;
    }


}