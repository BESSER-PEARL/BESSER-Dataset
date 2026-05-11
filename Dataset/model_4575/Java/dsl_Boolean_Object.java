





import java.util.List;
import java.util.ArrayList;

public class dsl_Boolean_Object extends Element {

    private boolean value;



    public dsl_Boolean_Object(
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