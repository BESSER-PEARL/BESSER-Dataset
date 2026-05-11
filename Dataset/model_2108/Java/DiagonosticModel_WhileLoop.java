





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_WhileLoop extends BlockAction {

    private String valueTo;
    private String operator;
    private String value;



    public DiagonosticModel_WhileLoop(
        String valueTo,        String operator,        String value    ) {
        super(
        );
        this.valueTo = valueTo;
        this.operator = operator;
        this.value = value;
    }


    public String getValueto() {
        return valueTo;
    }

    public void setValueto(String valueTo) {
        this.valueTo = valueTo;
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