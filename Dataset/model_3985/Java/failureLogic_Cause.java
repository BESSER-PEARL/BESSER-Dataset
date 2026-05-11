





import java.util.List;
import java.util.ArrayList;

public class failureLogic_Cause extends BaseElement {

    private String causeType;





    private failureLogic_Failure failurelogic_failure;


    public failureLogic_Cause(
        String causeType    ) {
        super(
        );
        this.causeType = causeType;
    }


    public String getCausetype() {
        return causeType;
    }

    public void setCausetype(String causeType) {
        this.causeType = causeType;
    }

    public failureLogic_Failure getFailurelogic_failure() {
        return failurelogic_failure;
    }

    public void setFailurelogic_failure(failureLogic_Failure failurelogic_failure) {
        this.failurelogic_failure = failurelogic_failure;
    }

}