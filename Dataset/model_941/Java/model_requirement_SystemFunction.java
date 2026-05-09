





import java.util.List;
import java.util.ArrayList;

public class model_requirement_SystemFunction extends NonDomainElement, UnicaseModelElement {

    private String exception;
    private String output;
    private String input;



    public model_requirement_SystemFunction(
        String exception,        String output,        String input    ) {
        super(
        );
        this.exception = exception;
        this.output = output;
        this.input = input;
    }


    public String getException() {
        return exception;
    }

    public void setException(String exception) {
        this.exception = exception;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public String getInput() {
        return input;
    }

    public void setInput(String input) {
        this.input = input;
    }


}