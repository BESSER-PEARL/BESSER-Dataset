





import java.util.List;
import java.util.ArrayList;

public class logiclanguage_IntLiteral extends AtomicTerm {

    private int value;



    public logiclanguage_IntLiteral(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}