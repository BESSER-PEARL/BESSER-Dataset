





import java.util.List;
import java.util.ArrayList;

public class mMDSL_OperatorAssign  {

    private String assign;





    private mMDSL_Variable mmdsl_variable;


    public mMDSL_OperatorAssign(
        String assign    ) {
        this.assign = assign;
    }


    public String getAssign() {
        return assign;
    }

    public void setAssign(String assign) {
        this.assign = assign;
    }

    public mMDSL_Variable getMmdsl_variable() {
        return mmdsl_variable;
    }

    public void setMmdsl_variable(mMDSL_Variable mmdsl_variable) {
        this.mmdsl_variable = mmdsl_variable;
    }

}