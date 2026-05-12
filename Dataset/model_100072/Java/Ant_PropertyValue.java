





import java.util.List;
import java.util.ArrayList;

public class Ant_PropertyValue extends PropertyName {

    private String value;



    public Ant_PropertyValue(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}