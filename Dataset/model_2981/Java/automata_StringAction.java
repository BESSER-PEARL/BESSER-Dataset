





import java.util.List;
import java.util.ArrayList;

public class automata_StringAction extends Action {

    private String value;





    private automata_StringVariable automata_stringvariable;


    public automata_StringAction(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public automata_StringVariable getAutomata_stringvariable() {
        return automata_stringvariable;
    }

    public void setAutomata_stringvariable(automata_StringVariable automata_stringvariable) {
        this.automata_stringvariable = automata_stringvariable;
    }

}