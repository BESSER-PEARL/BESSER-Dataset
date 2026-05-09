





import java.util.List;
import java.util.ArrayList;

public class sgen_BoolLiteral extends Literal {

    private boolean value;



    public sgen_BoolLiteral(
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