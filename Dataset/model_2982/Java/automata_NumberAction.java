





import java.util.List;
import java.util.ArrayList;

public class automata_NumberAction extends Action {

    private String value;





    private automata_NumberVariable automata_numbervariable;


    public automata_NumberAction(
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

    public automata_NumberVariable getAutomata_numbervariable() {
        return automata_numbervariable;
    }

    public void setAutomata_numbervariable(automata_NumberVariable automata_numbervariable) {
        this.automata_numbervariable = automata_numbervariable;
    }

}