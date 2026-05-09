





import java.util.List;
import java.util.ArrayList;

public class ea_automata_Module  {






    private List<Automaton> automatons;


    public ea_automata_Module(
    ) {
        this.automatons = new ArrayList<>();
    }

    public ea_automata_Module(
        ArrayList<Automaton> automatons    ) {
        this.automatons = automatons;
    }


    public List<Automaton> getAutomatons() {
        return automatons;
    }

    public void addAutomaton(Automaton automaton) {
        this.automatons.add(automaton);
    }

}