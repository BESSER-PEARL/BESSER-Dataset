





import java.util.List;
import java.util.ArrayList;

public class type_SimpleAnyType extends AnyType {

    private String value;
    private String rawValue;



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


}