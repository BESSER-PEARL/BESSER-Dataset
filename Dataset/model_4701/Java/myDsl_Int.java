





import java.util.List;
import java.util.ArrayList;

public class myDsl_Int extends TopLevelCmd, Expr {

    private int value;



    public myDsl_Int(
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