





import java.util.List;
import java.util.ArrayList;

public class model_requirement_UseCase extends UnicaseModelElement {

    private String rules;
    private String precondition;
    private String exception;
    private String postcondition;



    public model_requirement_UseCase(
        String rules,        String precondition,        String exception,        String postcondition    ) {
        super(
        );
        this.rules = rules;
        this.precondition = precondition;
        this.exception = exception;
        this.postcondition = postcondition;
    }


    public String getRules() {
        return rules;
    }

    public void setRules(String rules) {
        this.rules = rules;
    }
    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }
    public String getException() {
        return exception;
    }

    public void setException(String exception) {
        this.exception = exception;
    }
    public String getPostcondition() {
        return postcondition;
    }

    public void setPostcondition(String postcondition) {
        this.postcondition = postcondition;
    }


}