





import java.util.List;
import java.util.ArrayList;

public class forms_entityModeling_CompositeCondition extends Condition {

    private String booleanOperator;



    public forms_entityModeling_CompositeCondition(
        String booleanOperator    ) {
        super(
        );
        this.booleanOperator = booleanOperator;
    }


    public String getBooleanoperator() {
        return booleanOperator;
    }

    public void setBooleanoperator(String booleanOperator) {
        this.booleanOperator = booleanOperator;
    }


}