





import java.util.List;
import java.util.ArrayList;

public class model_requirement_UseCase extends UnicaseModelElement {

    private String rules;
    private String exception;
    private String precondition;
    private String postcondition;



    public model_requirement_UseCase(
        String rules,        String exception,        String precondition,        String postcondition    ) {
        super(
        );
        this.rules = rules;
        this.exception = exception;
        this.precondition = precondition;
        this.postcondition = postcondition;
    }


    public String getRules() {
        return rules;
    }

    public void setRules(String rules) {
        this.rules = rules;
    }
    public String getException() {
        return exception;
    }

    public void setException(String exception) {
        this.exception = exception;
    }
    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }
    public String getPostcondition() {
        return postcondition;
    }

    public void setPostcondition(String postcondition) {
        this.postcondition = postcondition;
    }


}