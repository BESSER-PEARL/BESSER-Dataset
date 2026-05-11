





import java.util.List;
import java.util.ArrayList;

public class autopl_Transition  {

    private String probability;





    private autopl_State autopl_state;




    private autopl_Symbol autopl_symbol;




    private autopl_Symbol autopl_symbol;




    private autopl_Symbol autopl_symbol;




    private autopl_State autopl_state;




    private autopl_Automaton autopl_automaton;




    private List<autopl_Symbol> autopl_symbols;


    public autopl_Transition(
        String probability    ) {
        this.probability = probability;
        this.autopl_symbols = new ArrayList<>();
    }

    public autopl_Transition(
        String probability        ArrayList<autopl_Symbol> autopl_symbols    ) {
        this.probability = probability;
        this.autopl_symbols = autopl_symbols;
    }

    public String getProbability() {
        return probability;
    }

    public void setProbability(String probability) {
        this.probability = probability;
    }

    public autopl_State getAutopl_state() {
        return autopl_state;
    }

    public void setAutopl_state(autopl_State autopl_state) {
        this.autopl_state = autopl_state;
    }
    public autopl_Symbol getAutopl_symbol() {
        return autopl_symbol;
    }

    public void setAutopl_symbol(autopl_Symbol autopl_symbol) {
        this.autopl_symbol = autopl_symbol;
    }
    public autopl_Symbol getAutopl_symbol() {
        return autopl_symbol;
    }

    public void setAutopl_symbol(autopl_Symbol autopl_symbol) {
        this.autopl_symbol = autopl_symbol;
    }
    public autopl_Symbol getAutopl_symbol() {
        return autopl_symbol;
    }

    public void setAutopl_symbol(autopl_Symbol autopl_symbol) {
        this.autopl_symbol = autopl_symbol;
    }
    public autopl_State getAutopl_state() {
        return autopl_state;
    }

    public void setAutopl_state(autopl_State autopl_state) {
        this.autopl_state = autopl_state;
    }
    public autopl_Automaton getAutopl_automaton() {
        return autopl_automaton;
    }

    public void setAutopl_automaton(autopl_Automaton autopl_automaton) {
        this.autopl_automaton = autopl_automaton;
    }
    public List<autopl_Symbol> getAutopl_symbols() {
        return autopl_symbols;
    }

    public void addAutopl_symbol(Autopl_symbol autopl_symbol) {
        this.autopl_symbols.add(autopl_symbol);
    }

}