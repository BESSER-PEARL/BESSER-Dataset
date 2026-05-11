





import java.util.List;
import java.util.ArrayList;

public class model_StringValue extends Value {

    private String value;
    private boolean null;



    public model_StringValue(
        String value,        boolean null    ) {
        super(
        );
        this.value = value;
        this.null = null;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getNull() {
        return null;
    }

    public void setNull(boolean null) {
        this.null = null;
    }


}