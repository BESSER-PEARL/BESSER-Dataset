





import java.util.List;
import java.util.ArrayList;

public class testintentionsAssistance_TestIntention extends AbstractElement {

    private String description;





    private List<testintentionsAssistance_Expression> testintentionsassistance_expressions;




    private testintentionsAssistance_OutVariable testintentionsassistance_outvariable;


    public testintentionsAssistance_TestIntention(
        String description    ) {
        super(
        );
        this.description = description;
        this.testintentionsassistance_expressions = new ArrayList<>();
    }

    public testintentionsAssistance_TestIntention(
        String description        ArrayList<testintentionsAssistance_Expression> testintentionsassistance_expressions    ) {
        this.description = description;
        this.testintentionsassistance_expressions = testintentionsassistance_expressions;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<testintentionsAssistance_Expression> getTestintentionsassistance_expressions() {
        return testintentionsassistance_expressions;
    }

    public void addTestintentionsassistance_expression(Testintentionsassistance_expression testintentionsassistance_expression) {
        this.testintentionsassistance_expressions.add(testintentionsassistance_expression);
    }
    public testintentionsAssistance_OutVariable getTestintentionsassistance_outvariable() {
        return testintentionsassistance_outvariable;
    }

    public void setTestintentionsassistance_outvariable(testintentionsAssistance_OutVariable testintentionsassistance_outvariable) {
        this.testintentionsassistance_outvariable = testintentionsassistance_outvariable;
    }

}