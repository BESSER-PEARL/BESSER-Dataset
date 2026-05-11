





import java.util.List;
import java.util.ArrayList;

public class datatype_BooleanPropertyAttribute extends PropertyAttribute {

    private String type;
    private boolean value;



    public datatype_BooleanPropertyAttribute(
        String type,        boolean value    ) {
        super(
        );
        this.type = type;
        this.value = value;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}