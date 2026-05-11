





import java.util.List;
import java.util.ArrayList;

public class automata_StringGuard extends Guard {

    private String operator;
    private String value;



    public automata_StringGuard(
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


}