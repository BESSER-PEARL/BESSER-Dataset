





import java.util.List;
import java.util.ArrayList;

public class datatype_BooleanPropertyAttribute extends PropertyAttribute {

    private boolean value;
    private String type;



    public datatype_BooleanPropertyAttribute(
        boolean value,        String type    ) {
        super(
        );
        this.value = value;
        this.type = type;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}