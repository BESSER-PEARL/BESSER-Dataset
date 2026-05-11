





import java.util.List;
import java.util.ArrayList;

public class exercises_Transition extends NamableElement {

    private String input;





    private exercises_DFA exercises_dfa;


    public exercises_Transition(
        String input    ) {
        super(
        );
        this.input = input;
    }


    public String getInput() {
        return input;
    }

    public void setInput(String input) {
        this.input = input;
    }

    public exercises_DFA getExercises_dfa() {
        return exercises_dfa;
    }

    public void setExercises_dfa(exercises_DFA exercises_dfa) {
        this.exercises_dfa = exercises_dfa;
    }

}