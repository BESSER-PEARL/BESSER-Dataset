





import java.util.List;
import java.util.ArrayList;

public class automata_State  {

    private String name;





    private automata_Automata automata_automata;




    private automata_Initial automata_initial;




    private automata_Current automata_current;


    public automata_State(
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
    public automata_Initial getAutomata_initial() {
        return automata_initial;
    }

    public void setAutomata_initial(automata_Initial automata_initial) {
        this.automata_initial = automata_initial;
    }
    public automata_Current getAutomata_current() {
        return automata_current;
    }

    public void setAutomata_current(automata_Current automata_current) {
        this.automata_current = automata_current;
    }

}