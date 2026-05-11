





import java.util.List;
import java.util.ArrayList;

public class fiacre_LocalVariable extends Variable {

    private boolean constant;



    public fiacre_LocalVariable(
        boolean constant    ) {
        super(
        );
        this.constant = constant;
    }


    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }


}