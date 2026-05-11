





import java.util.List;
import java.util.ArrayList;

public class automata_BooleanGuard extends Guard {

    private boolean value;
    private String operator;



    public automata_BooleanGuard(
        boolean value,        String operator    ) {
        super(
        );
        this.value = value;
        this.operator = operator;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }


}