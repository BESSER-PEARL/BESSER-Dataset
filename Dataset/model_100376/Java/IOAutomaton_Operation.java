





import java.util.List;
import java.util.ArrayList;

public class IOAutomaton_Operation  {

    private String name;





    private IOAutomaton_Input ioautomaton_input;




    private IOAutomaton_Output ioautomaton_output;


    public IOAutomaton_Operation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public IOAutomaton_Input getIoautomaton_input() {
        return ioautomaton_input;
    }

    public void setIoautomaton_input(IOAutomaton_Input ioautomaton_input) {
        this.ioautomaton_input = ioautomaton_input;
    }
    public IOAutomaton_Output getIoautomaton_output() {
        return ioautomaton_output;
    }

    public void setIoautomaton_output(IOAutomaton_Output ioautomaton_output) {
        this.ioautomaton_output = ioautomaton_output;
    }

}