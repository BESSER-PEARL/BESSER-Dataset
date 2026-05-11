





import java.util.List;
import java.util.ArrayList;

public class presentation_literal_BooleanLiteral extends GeneralLiteral {

    private boolean value;



    public presentation_literal_BooleanLiteral(
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