





import java.util.List;
import java.util.ArrayList;

public class statemachine_StateMachine  {






    private List<statemachine_Declaration> statemachine_declarations;


    public statemachine_StateMachine(
    ) {
        this.statemachine_declarations = new ArrayList<>();
    }

    public statemachine_StateMachine(
        ArrayList<statemachine_Declaration> statemachine_declarations    ) {
        this.statemachine_declarations = statemachine_declarations;
    }


    public List<statemachine_Declaration> getStatemachine_declarations() {
        return statemachine_declarations;
    }

    public void addStatemachine_declaration(Statemachine_declaration statemachine_declaration) {
        this.statemachine_declarations.add(statemachine_declaration);
    }

}