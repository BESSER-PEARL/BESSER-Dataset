





import java.util.List;
import java.util.ArrayList;

public class type_SimpleAnyType extends AnyType {

    private String rawValue;
    private String value;



    public type_SimpleAnyType(
        String rawValue,        String value    ) {
        super(
        );
        this.rawValue = rawValue;
        this.value = value;
    }


    public String getRawvalue() {
        return rawValue;
    }

    public void setRawvalue(String rawValue) {
        this.rawValue = rawValue;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}