





import java.util.List;
import java.util.ArrayList;

public class automata_BooleanAction extends Action {

    private boolean value;





    private automata_BooleanVariable automata_booleanvariable;


    public automata_BooleanAction(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }

    public automata_BooleanVariable getAutomata_booleanvariable() {
        return automata_booleanvariable;
    }

    public void setAutomata_booleanvariable(automata_BooleanVariable automata_booleanvariable) {
        this.automata_booleanvariable = automata_booleanvariable;
    }

}