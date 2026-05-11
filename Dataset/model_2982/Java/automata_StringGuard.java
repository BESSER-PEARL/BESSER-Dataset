





import java.util.List;
import java.util.ArrayList;

public class automata_StringGuard extends Guard {

    private String value;
    private boolean operator;





    private automata_StringVariable automata_stringvariable;


    public automata_StringGuard(
        String value,        boolean operator    ) {
        super(
        );
        this.value = value;
        this.operator = operator;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getOperator() {
        return operator;
    }

    public void setOperator(boolean operator) {
        this.operator = operator;
    }

    public automata_StringVariable getAutomata_stringvariable() {
        return automata_stringvariable;
    }

    public void setAutomata_stringvariable(automata_StringVariable automata_stringvariable) {
        this.automata_stringvariable = automata_stringvariable;
    }

}