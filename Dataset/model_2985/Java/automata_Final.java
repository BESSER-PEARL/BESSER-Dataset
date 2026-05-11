





import java.util.List;
import java.util.ArrayList;

public class automata_Final  {

    private String name;





    private automata_State automata_state;


    public automata_Final(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public automata_State getAutomata_state() {
        return automata_state;
    }

    public void setAutomata_state(automata_State automata_state) {
        this.automata_state = automata_state;
    }

}