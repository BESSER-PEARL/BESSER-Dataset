





import java.util.List;
import java.util.ArrayList;

public class Logo_Boolean extends Literal {

    private boolean value;



    public Logo_Boolean(
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