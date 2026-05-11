





import java.util.List;
import java.util.ArrayList;

public class table_description_BackgroundConditionalStyle  {

    private String predicateExpression;





    private BackgroundStyleDescription backgroundstyledescription;


    public table_description_BackgroundConditionalStyle(
        String predicateExpression    ) {
        this.predicateExpression = predicateExpression;
    }


    public String getPredicateexpression() {
        return predicateExpression;
    }

    public void setPredicateexpression(String predicateExpression) {
        this.predicateExpression = predicateExpression;
    }

    public BackgroundStyleDescription getBackgroundstyledescription() {
        return backgroundstyledescription;
    }

    public void setBackgroundstyledescription(BackgroundStyleDescription backgroundstyledescription) {
        this.backgroundstyledescription = backgroundstyledescription;
    }

}