





import java.util.List;
import java.util.ArrayList;

public class model_requirement_SystemFunction extends NonDomainElement, UnicaseModelElement {

    private String output;
    private String exception;
    private String input;



    public model_requirement_SystemFunction(
        String output,        String exception,        String input    ) {
        super(
        );
        this.output = output;
        this.exception = exception;
        this.input = input;
    }


    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public String getException() {
        return exception;
    }

    public void setException(String exception) {
        this.exception = exception;
    }
    public String getInput() {
        return input;
    }

    public void setInput(String input) {
        this.input = input;
    }


}