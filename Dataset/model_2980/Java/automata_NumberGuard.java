





import java.util.List;
import java.util.ArrayList;

public class automata_NumberGuard extends Guard {

    private String value;
    private String operator;



    public automata_NumberGuard(
        String value,        String operator    ) {
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
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }


}