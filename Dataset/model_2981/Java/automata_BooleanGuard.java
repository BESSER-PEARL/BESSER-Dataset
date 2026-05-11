





import java.util.List;
import java.util.ArrayList;

public class automata_BooleanGuard extends Guard {

    private String operator;
    private boolean value;





    private automata_BooleanVariable automata_booleanvariable;


    public automata_BooleanGuard(
        String operator,        boolean value    ) {
        super(
        );
        this.operator = operator;
        this.value = value;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
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