





import java.util.List;
import java.util.ArrayList;

public class logiclanguage_BoolLiteral extends AtomicTerm {

    private boolean value;



    public logiclanguage_BoolLiteral(
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