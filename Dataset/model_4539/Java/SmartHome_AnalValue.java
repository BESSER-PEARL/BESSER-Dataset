





import java.util.List;
import java.util.ArrayList;

public class SmartHome_AnalValue extends Value {

    private boolean value;



    public SmartHome_AnalValue(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}