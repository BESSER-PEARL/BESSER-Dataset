





import java.util.List;
import java.util.ArrayList;

public class camel_type_EnumerateValue extends SingleValue {

    private int value;
    private String name;



    public camel_type_EnumerateValue(
        int value,        String name    ) {
        super(
        );
        this.value = value;
        this.name = name;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}