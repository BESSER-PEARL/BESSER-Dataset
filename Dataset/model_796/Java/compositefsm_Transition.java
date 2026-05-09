





import java.util.List;
import java.util.ArrayList;

public class compositefsm_Transition  {

    private String input;
    private String output;



    public compositefsm_Transition(
        String input,        String output    ) {
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