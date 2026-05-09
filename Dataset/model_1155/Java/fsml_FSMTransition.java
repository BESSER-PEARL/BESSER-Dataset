





import java.util.List;
import java.util.ArrayList;

public class fsml_FSMTransition  {

    private String action;
    private String input;



    public fsml_FSMTransition(
        String action,        String input    ) {
        this.action = action;
        this.input = input;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getInput() {
        return input;
    }

    public void setInput(String input) {
        this.input = input;
    }


}