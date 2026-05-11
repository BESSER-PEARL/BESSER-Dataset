





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_IntegerLit extends Literal {

    private int value;



    public CompleteDSLPckg_IntegerLit(
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