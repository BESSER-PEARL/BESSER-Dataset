





import java.util.List;
import java.util.ArrayList;

public class exercises_State extends NamableElement {

    private boolean isEnd;
    private String id;
    private boolean isStart;





    private List<exercises_Transition> exercises_transitions;




    private exercises_DFA exercises_dfa;




    private List<exercises_Transition> exercises_transitions;


    public exercises_State(
        boolean isEnd,        String id,        boolean isStart    ) {
        super(
        );
        this.isEnd = isEnd;
        this.id = id;
        this.isStart = isStart;
        this.exercises_transitions = new ArrayList<>();
        this.exercises_transitions = new ArrayList<>();
    }

    public exercises_State(
        boolean isEnd,        String id,        boolean isStart        ArrayList<exercises_Transition> exercises_transitions,        ArrayList<exercises_Transition> exercises_transitions    ) {
        this.isEnd = isEnd;
        this.id = id;
        this.isStart = isStart;
        this.exercises_transitions = exercises_transitions;
        this.exercises_transitions = exercises_transitions;
    }

    public boolean getIsend() {
        return isEnd;
    }

    public void setIsend(boolean isEnd) {
        this.isEnd = isEnd;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getIsstart() {
        return isStart;
    }

    public void setIsstart(boolean isStart) {
        this.isStart = isStart;
    }

    public List<exercises_Transition> getExercises_transitions() {
        return exercises_transitions;
    }

    public void addExercises_transition(Exercises_transition exercises_transition) {
        this.exercises_transitions.add(exercises_transition);
    }
    public exercises_DFA getExercises_dfa() {
        return exercises_dfa;
    }

    public void setExercises_dfa(exercises_DFA exercises_dfa) {
        this.exercises_dfa = exercises_dfa;
    }
    public List<exercises_Transition> getExercises_transitions() {
        return exercises_transitions;
    }

    public void addExercises_transition(Exercises_transition exercises_transition) {
        this.exercises_transitions.add(exercises_transition);
    }

}