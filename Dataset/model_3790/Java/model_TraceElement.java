





import java.util.List;
import java.util.ArrayList;

public class model_TraceElement  {

    private String message;





    private model_TestProblem model_testproblem;


    public model_TraceElement(
        String message    ) {
        this.message = message;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public model_TestProblem getModel_testproblem() {
        return model_testproblem;
    }

    public void setModel_testproblem(model_TestProblem model_testproblem) {
        this.model_testproblem = model_testproblem;
    }

}