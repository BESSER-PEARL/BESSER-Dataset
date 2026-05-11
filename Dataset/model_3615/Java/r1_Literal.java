





import java.util.List;
import java.util.ArrayList;

public class r1_Literal extends Expression {

    private String value;
    private String valueType;



    public r1_Literal(
        String value,        String valueType    ) {
        super(
        );
        this.value = value;
        this.valueType = valueType;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getValuetype() {
        return valueType;
    }

    public void setValuetype(String valueType) {
        this.valueType = valueType;
    }


}