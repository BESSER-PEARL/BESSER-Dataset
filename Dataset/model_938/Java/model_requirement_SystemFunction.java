





import java.util.List;
import java.util.ArrayList;

public class model_requirement_SystemFunction extends NonDomainElement, UnicaseModelElement {

    private String output;
    private String input;
    private String exception;



    public model_requirement_SystemFunction(
        String output,        String input,        String exception    ) {
        super(
        );
        this.output = output;
        this.input = input;
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
    public String getException() {
        return exception;
    }

    public void setException(String exception) {
        this.exception = exception;
    }


}