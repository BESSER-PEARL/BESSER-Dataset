





import java.util.List;
import java.util.ArrayList;

public class autopl_Symbol  {

    private String name;





    private autopl_Alphabet autopl_alphabet;




    private autopl_Automaton autopl_automaton;


    public autopl_Symbol(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public autopl_Alphabet getAutopl_alphabet() {
        return autopl_alphabet;
    }

    public void setAutopl_alphabet(autopl_Alphabet autopl_alphabet) {
        this.autopl_alphabet = autopl_alphabet;
    }
    public autopl_Automaton getAutopl_automaton() {
        return autopl_automaton;
    }

    public void setAutopl_automaton(autopl_Automaton autopl_automaton) {
        this.autopl_automaton = autopl_automaton;
    }

}