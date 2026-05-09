





import java.util.List;
import java.util.ArrayList;

public class type_SimpleAnyType extends AnyType {

    private String value;
    private String rawValue;





    private type_EDataType type_edatatype;


    public type_SimpleAnyType(
        String value,        String rawValue    ) {
        super(
        );
        this.value = value;
        this.rawValue = rawValue;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getRawvalue() {
        return rawValue;
    }

    public void setRawvalue(String rawValue) {
        this.rawValue = rawValue;
    }

    public type_EDataType getType_edatatype() {
        return type_edatatype;
    }

    public void setType_edatatype(type_EDataType type_edatatype) {
        this.type_edatatype = type_edatatype;
    }

}