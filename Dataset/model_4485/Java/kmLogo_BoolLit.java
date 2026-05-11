





import java.util.List;
import java.util.ArrayList;

public class kmLogo_BoolLit extends Literal {

    private boolean value;



    public kmLogo_BoolLit(
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