





import java.util.List;
import java.util.ArrayList;

public class caltrop_StateVariable extends Variable {

    private boolean constant;



    public caltrop_StateVariable(
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