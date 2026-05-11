





import java.util.List;
import java.util.ArrayList;

public class base_PropertyAccess extends Access {

    private String value;



    public base_PropertyAccess(
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