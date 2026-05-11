





import java.util.List;
import java.util.ArrayList;

public class r1_Literal extends Expression {

    private String valueType;
    private String value;



    public r1_Literal(
        String valueType,        String value    ) {
        super(
        );
        this.valueType = valueType;
        this.value = value;
    }


    public String getValuetype() {
        return valueType;
    }

    public void setValuetype(String valueType) {
        this.valueType = valueType;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}