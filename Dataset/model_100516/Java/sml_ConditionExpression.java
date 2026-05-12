





import java.util.List;
import java.util.ArrayList;

public class sml_ConditionExpression  {






    private sml_Expression sml_expression;




    private sml_LoopCondition sml_loopcondition;




    private sml_Condition sml_condition;




    private sml_CaseCondition sml_casecondition;


    public sml_ConditionExpression(
    ) {
    }



    public sml_Expression getSml_expression() {
        return sml_expression;
    }

    public void setSml_expression(sml_Expression sml_expression) {
        this.sml_expression = sml_expression;
    }
    public sml_LoopCondition getSml_loopcondition() {
        return sml_loopcondition;
    }

    public void setSml_loopcondition(sml_LoopCondition sml_loopcondition) {
        this.sml_loopcondition = sml_loopcondition;
    }
    public sml_Condition getSml_condition() {
        return sml_condition;
    }

    public void setSml_condition(sml_Condition sml_condition) {
        this.sml_condition = sml_condition;
    }
    public sml_CaseCondition getSml_casecondition() {
        return sml_casecondition;
    }

    public void setSml_casecondition(sml_CaseCondition sml_casecondition) {
        this.sml_casecondition = sml_casecondition;
    }

}