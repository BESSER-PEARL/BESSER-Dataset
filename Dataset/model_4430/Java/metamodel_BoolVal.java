





import java.util.List;
import java.util.ArrayList;

public class metamodel_BoolVal extends Type {

    private boolean value;



    public metamodel_BoolVal(
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