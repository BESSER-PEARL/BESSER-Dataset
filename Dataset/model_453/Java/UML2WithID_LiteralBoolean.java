





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_LiteralBoolean extends LiteralSpecification {

    private boolean value;



    public UML2WithID_LiteralBoolean(
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