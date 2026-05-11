





import java.util.List;
import java.util.ArrayList;

public class automata_Initial  {

    private String name;





    private automata_Automata automata_automata;




    private automata_State automata_state;


    public automata_Initial(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public automata_Automata getAutomata_automata() {
        return automata_automata;
    }

    public void setAutomata_automata(automata_Automata automata_automata) {
        this.automata_automata = automata_automata;
    }
    public automata_State getAutomata_state() {
        return automata_state;
    }

    public void setAutomata_state(automata_State automata_state) {
        this.automata_state = automata_state;
    }

}