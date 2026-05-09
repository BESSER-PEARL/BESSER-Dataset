





import java.util.List;
import java.util.ArrayList;

public class fsm_Transition extends NamedElement {

    private String input;
    private String output;



    public fsm_Transition(
        String input,        String output    ) {
        super(
        );
        this.input = input;
        this.output = output;
    }


    public String getInput() {
        return input;
    }

    public void setInput(String input) {
        this.input = input;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }


}