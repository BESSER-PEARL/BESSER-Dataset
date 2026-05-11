





import java.util.List;
import java.util.ArrayList;

public class prolog_AtomicNumber extends Term {

    private int value;



    public prolog_AtomicNumber(
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