





import java.util.List;
import java.util.ArrayList;

public class UML2_LiteralBoolean extends LiteralSpecification {

    private boolean value;



    public UML2_LiteralBoolean(
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