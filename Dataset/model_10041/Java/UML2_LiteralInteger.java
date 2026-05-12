





import java.util.List;
import java.util.ArrayList;

public class UML2_LiteralInteger extends LiteralSpecification {

    private int value;



    public UML2_LiteralInteger(
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