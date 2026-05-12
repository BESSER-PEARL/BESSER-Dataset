





import java.util.List;
import java.util.ArrayList;

public class IOAutomaton_ReturnValue  {

    private String name;
    private boolean isVoid;





    private IOAutomaton_Activation ioautomaton_activation;




    private IOAutomaton_Output ioautomaton_output;


    public IOAutomaton_ReturnValue(
        String name,        boolean isVoid    ) {
        this.name = name;
        this.isVoid = isVoid;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsvoid() {
        return isVoid;
    }

    public void setIsvoid(boolean isVoid) {
        this.isVoid = isVoid;
    }

    public IOAutomaton_Activation getIoautomaton_activation() {
        return ioautomaton_activation;
    }

    public void setIoautomaton_activation(IOAutomaton_Activation ioautomaton_activation) {
        this.ioautomaton_activation = ioautomaton_activation;
    }
    public IOAutomaton_Output getIoautomaton_output() {
        return ioautomaton_output;
    }

    public void setIoautomaton_output(IOAutomaton_Output ioautomaton_output) {
        this.ioautomaton_output = ioautomaton_output;
    }

}