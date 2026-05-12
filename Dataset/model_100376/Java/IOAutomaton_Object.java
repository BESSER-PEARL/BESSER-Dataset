





import java.util.List;
import java.util.ArrayList;

public class IOAutomaton_Object  {

    private String name;





    private IOAutomaton_Output ioautomaton_output;


    public IOAutomaton_Object(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public IOAutomaton_Output getIoautomaton_output() {
        return ioautomaton_output;
    }

    public void setIoautomaton_output(IOAutomaton_Output ioautomaton_output) {
        this.ioautomaton_output = ioautomaton_output;
    }

}