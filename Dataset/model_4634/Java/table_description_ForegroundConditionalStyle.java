





import java.util.List;
import java.util.ArrayList;

public class table_description_ForegroundConditionalStyle  {

    private String predicateExpression;





    private ForegroundStyleDescription foregroundstyledescription;


    public table_description_ForegroundConditionalStyle(
        String predicateExpression    ) {
        this.predicateExpression = predicateExpression;
    }


    public String getPredicateexpression() {
        return predicateExpression;
    }

    public void setPredicateexpression(String predicateExpression) {
        this.predicateExpression = predicateExpression;
    }

    public ForegroundStyleDescription getForegroundstyledescription() {
        return foregroundstyledescription;
    }

    public void setForegroundstyledescription(ForegroundStyleDescription foregroundstyledescription) {
        this.foregroundstyledescription = foregroundstyledescription;
    }

}