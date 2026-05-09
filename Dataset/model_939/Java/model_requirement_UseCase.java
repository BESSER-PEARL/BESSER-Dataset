





import java.util.List;
import java.util.ArrayList;

public class model_requirement_UseCase extends UnicaseModelElement {

    private String exception;
    private String precondition;
    private String rules;
    private String postcondition;



    public model_requirement_UseCase(
        String exception,        String precondition,        String rules,        String postcondition    ) {
        super(
        );
        this.exception = exception;
        this.precondition = precondition;
        this.rules = rules;
        this.postcondition = postcondition;
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
    public String getRules() {
        return rules;
    }

    public void setRules(String rules) {
        this.rules = rules;
    }
    public String getPostcondition() {
        return postcondition;
    }

    public void setPostcondition(String postcondition) {
        this.postcondition = postcondition;
    }


}