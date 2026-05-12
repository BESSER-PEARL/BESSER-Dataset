





import java.util.List;
import java.util.ArrayList;

public class IOAutomaton_Output  {

    private String name;





    private IOAutomaton_Activation ioautomaton_activation;


    public IOAutomaton_Output(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public IOAutomaton_Activation getIoautomaton_activation() {
        return ioautomaton_activation;
    }

    public void setIoautomaton_activation(IOAutomaton_Activation ioautomaton_activation) {
        this.ioautomaton_activation = ioautomaton_activation;
    }

}