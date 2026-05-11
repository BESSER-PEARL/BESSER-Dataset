





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_BoolVal extends Expression {

    private boolean value;



    public dinkiemodel_BoolVal(
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