





import java.util.List;
import java.util.ArrayList;

public class automata_NumberGuard extends Guard {

    private String operator;
    private String value;





    private automata_NumberVariable automata_numbervariable;


    public automata_NumberGuard(
        String operator,        String value    ) {
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