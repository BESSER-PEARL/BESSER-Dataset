





import java.util.List;
import java.util.ArrayList;

public class myDsl_Bool extends TopLevelCmd, Expr {

    private boolean value;



    public myDsl_Bool(
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