





import java.util.List;
import java.util.ArrayList;

public class dmx_DmxBooleanLiteral extends DExpression {

    private boolean value;



    public dmx_DmxBooleanLiteral(
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