





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlBooleanLiteral extends SadlExplicitValueLiteral {

    private boolean truethy;



    public sADL_SadlBooleanLiteral(
        boolean truethy    ) {
        super(
        );
        this.truethy = truethy;
    }


    public boolean getTruethy() {
        return truethy;
    }

    public void setTruethy(boolean truethy) {
        this.truethy = truethy;
    }


}