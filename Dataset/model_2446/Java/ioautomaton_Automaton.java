





import java.util.List;
import java.util.ArrayList;

public class ioautomaton_Automaton  {

    private String sender;





    private ioautomaton_AutomatonContainer ioautomaton_automatoncontainer;


    public ioautomaton_Automaton(
        String sender    ) {
        this.sender = sender;
    }


    public String getSender() {
        return sender;
    }

    public void setSender(String sender) {
        this.sender = sender;
    }

    public ioautomaton_AutomatonContainer getIoautomaton_automatoncontainer() {
        return ioautomaton_automatoncontainer;
    }

    public void setIoautomaton_automatoncontainer(ioautomaton_AutomatonContainer ioautomaton_automatoncontainer) {
        this.ioautomaton_automatoncontainer = ioautomaton_automatoncontainer;
    }

}