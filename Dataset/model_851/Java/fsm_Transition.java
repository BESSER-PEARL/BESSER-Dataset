





import java.util.List;
import java.util.ArrayList;

public class fsm_Transition  {

    private String output;
    private String input;



    public fsm_Transition(
        String output,        String input    ) {
        this.output = output;
        this.input = input;
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